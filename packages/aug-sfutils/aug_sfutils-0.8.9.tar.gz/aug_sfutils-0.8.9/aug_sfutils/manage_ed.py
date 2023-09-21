import os, struct, logging, traceback
import numpy as np
from aug_sfutils import config

logger = logging.getLogger('aug_sfutils.manage_ed')
logger.level = logging.INFO
#logger.level = logging.DEBUG


def sf_path(nshot, diag, exp='AUGD', ed=0):
    """Path finder for shotfiles

    Input:
        nshot    int  Shotnumber
        diag     str  Diagnostic label
        exp(opt) str  Expriment label (default: 'AUGD')
        ed(opt)  int  Edition number (default: 0)

    Output:
        path_out   str   Full path of shotfile (None if not found)
        ed         int   Actual edition (non trivial if input ed=0)
    """

    sshot = str(nshot).zfill(5)
    exp = exp.lower()
    diag = diag.upper()

    logger.debug('Edition %d', ed)
    if ed == 0:
        ed = find_last_ed(nshot, diag, exp=exp)
    if ed is None:
        return None, None

    path1 = '%s/%s/%s/%s' %(config.sfBasepath, exp, diag, sshot[:2])
    if os.path.isdir(path1):
        if ed == -1:
            path_out = '%s/%05d' %(path1, nshot)
        else:
            path_out = '%s/%05d.%d' %(path1, nshot, ed)
    return path_out, ed


def find_last_ed(nshot, diag, exp='augd'):
    """Finds the actual edition number of ed=0
    Input:
        nshot    int  Shotnumber
        diag     str  Diagnostic label
        exp(opt) str  Expriment label (default: 'AUGD')

    Output:
        ed_nr    int  Actual edition number. -1 for level0, None if not found
    """
 
    sshot = str(nshot).zfill(5)
    exp = exp.lower()
    diag = diag.upper()

    sf_dir = '%s/%s/%s/%s' %(config.sfBasepath, exp, diag, sshot[:2])
    if not os.path.isdir(sf_dir):
        return None # SF dir does not exist

    ed_list = []
    for fnam in os.listdir(sf_dir):
        if len(fnam) == 5:
            return -1 
        if fnam[:5] == sshot:
            ssho, ed = fnam.split('.')
            ed_list.append(int(ed))

    if ed_list:
        return max(ed_list)
    else:
        return None # SF dir exists, but no shotfiles for nshot

def ed_zero(diag, nshot, exp='augd'):
    """Finds the actual edition number of ed=0
    Input:
        nshot    int  Shotnumber
        diag     str  Diagnostic label
        exp(opt) str  Expriment label (default: 'AUGD')

    Output:
        ed_nr    int  Actual edition number. 1 for level0, None if not found
    """
 
    sshot = str(nshot).zfill(5)
    exp = exp.lower()
    diag = diag.upper()

    sf_dir = '%s/%s/%s/%s' %(config.sfBasepath, exp, diag, sshot[:2])
    if not os.path.isdir(sf_dir):
        print('SFDIR', sf_dir)
        return None

    for ed in range(1, 1000):
        sfpath = '%s/%s.%d' %(sf_dir, sshot, ed)
        if not os.path.isfile(sfpath):
            break
        print(sfpath)
    ed -= 1
    if ed == 0:
        return None
    else:
        return ed


def read_ed_cntl(fed_dir, exp='augd'):
    """Parser of ed_cntl file

    Input:
        fed_dir   str   Path where to look for ed_cntl file
        exp(opt)  str   Exp
    Output:
        max_ed    int   Max edition number for given diag, shot
    """
    ed_ctrl = '%s/ed_cntl' %fed_dir
    if not os.path.isfile(ed_ctrl):
        logger.error(ed_ctrl)
        return None

    exp = exp.strip().lower()
    if exp == 'augd':
        shot_byt  = 5
        delta_byt = 24
    else:
        shot_byt  = 3
        delta_byt = 20

    with open(ed_ctrl, 'rb') as f:
        byt_str = f.read()

    jbyt = 12
    max_ed = {}

    while(True):
        try:
            ed = struct.unpack('>I', byt_str[jbyt + 4: jbyt + 8])[0]
            shot = struct.unpack('>%dc' %shot_byt, byt_str[jbyt+16: jbyt+16+shot_byt])
            jbyt += delta_byt
            sshot = b''.join(shot)
            nshot = int(sshot)
            max_ed[nshot] = np.int32(ed)
        except:
            traceback.print_exc()
            break

    if len(max_ed.keys()) > 0:
        return max_ed
    else:
        return None
