"""Equilibrium object from shotfile"""

import logging
import numpy as np
from scipy.integrate import cumtrapz
from scipy.interpolate import interp1d
from scipy.constants import mu_0

from aug_sfutils import sfobj, SFREAD, parse_kwargs, time_slice

logger = logging.getLogger('aug_sfutils.sf2equ')

#--------------------------------
# COCOs
# https://crppwww.epfl.ch/~sauter/cocos/Sauter_COCOS_Tokamak_Coordinate_Conventions.pdf
# Table I page 8
#--------------------------------

sigma = { \
    'bp'       : [ 1,  1, -1, -1,  1,  1, -1, -1], \
    'rphiz'    : [ 1, -1,  1, -1,  1, -1,  1, -1], \
    'rhothephi': [ 1,  1, -1, -1, -1, -1,  1,  1]}

explain = {'rphiz'    : {1: '(R, phi, Z) r'    , -1: '(R, Z, phi) l'}, \
           'rhothephi': {1: '(rho, the, phi) r', -1: '(rho, phi, the) l'    } }

 
class EQU:
    """Reads the whole equilibrium shotfile
    Reduces 1D profiles to within separatrix,
    Calculates a few useful derived quantities
    Accepts a time sub-interval via tbeg, tend keywords
    """

    def __init__(self, nshot, **kwargs):

        """
        Input
        ---------
        nshot: int
            shot number
        diag: str
            diagnsotics used for mapping (EQI, EQH, ...)
        exp: str
            experiment (AUGD)
        ed:  int
            edition
        tbeg: float
            initial time [s]
        tend: float
            final time [s]
        """

        exp  = parse_kwargs.parse_kw( ('exp', 'experiment'), kwargs, default='AUGD')
        diag = parse_kwargs.parse_kw( ('diag', 'diagnostic'), kwargs, default='EQH')
        ed   = parse_kwargs.parse_kw( ('ed', 'edition'), kwargs, default=0)

        self.sf = SFREAD(nshot, diag, ed=ed, exp=exp)

        if self.sf.status:

            ## Shot number
            self.shot = nshot 

            ## Shotfile exp
            self.exp = exp
            
            ## Shotfile diag
            self.diag = diag

            ## Actual shotfile edition (> 0)
            self.ed = self.sf.ed

            ## COCO number
            self.cocos = 17

            ## Time grid of equilibrium shotfile
            self.time = self.sf.getobject('time')
            nt = len(self.time)
            parmv = self.sf.sf['PARMV'].data
            nR = parmv['M'].data + 1
            nZ = parmv['N'].data + 1
            ## R of PFM cartesian grid [m]
            self.Rmesh = self.sf.getobject('Ri')[: nR, 0]
            ## z of PFM cartesian grid [m]
            self.Zmesh = self.sf.getobject('Zj')[: nZ, 0]

            Lpf = self.sf.getobject('Lpf').T
            ## For 1D profiles: #points within separatrix
            self.lpfp = Lpf%10000 # inside sep
            ## For 1D profiles: #points in SOL
            self.lpfe = (Lpf - self.lpfp)//10000 #outside sep
            ## Spatial index sorted from inside to outside, at each time
            self.ind_sort = []
            for jt in range(nt):
                ind_core = np.arange(self.lpfp[jt], -1, -1)
                ind_sol  = np.arange(self.lpfp[jt] + 3, self.lpfp[jt] + 3 + self.lpfe[jt])
                self.ind_sort.append(np.append(ind_core, ind_sol))
        else:
            logger.error('Problems opening %s:%s:%d for shot %d' %(exp, diag, ed, nshot))
            return

        if 'tbeg' in kwargs.keys():
            tbeg = kwargs['tbeg']
        else:
            tbeg = np.min(self.time)
        if 'tend' in kwargs.keys():
            tend = kwargs['tend']
        else:
            tend = np.max(self.time)

        (self.indt, ) = np.where((self.time >= tbeg) & (self.time <= tend))
        if len(self.indt) == 0:
            self.indt = [np.argmin(np.abs(self.time - tbeg))]

        logger.info('Reading equ scalars')
        self.read_scalars()
        logger.info('Reading equ 1d profiles')
        self.read_profiles()
        logger.info('Reading equ PFM')
        self.read_pfm()

        logger.info('COCO %d' %self.cocos)

# Sign of Ip, Bt (positive=ccw from above), valid for COCO=17 (CLISTE)
        self.ip_ccw = np.sign((self.psix - self.psi0).mean())
        self.bt_ccw = np.sign(np.nanmean(self.jpol))

        jcoco = self.cocos%10 - 1
        ebp   = self.cocos//10
        self.psi_sign = -self.ip_ccw*sigma['bp'][jcoco]*sigma['rphiz'][jcoco]
        psi_2pi  = (2.*np.pi)**ebp
        self.psi_fac = self.psi_sign*psi_2pi
        self.phi_sign = self.bt_ccw*sigma['rphiz'][jcoco]

        self.time = self.time[self.indt]
        nt = len(self.time)
        if self.diag == 'IDE':
            nrho = np.max(self.lpfp)
        else:
            nrho = np.max(self.lpfp) + 1

        self.psi0 = self.psi0[self.indt]
        self.psix = self.psix[self.indt]
        self.psi_lcfs = self.pfl[self.indt, nrho]

        if hasattr(self, 'ipipsi'):
            self.ipipsi = self.ipipsi[self.indt]

        for key in self.ssqnames:
            self.__dict__[key] = self.__dict__[key][self.indt]
        for key in ('pfl', 'tfl', 'ffp', 'rinv', 'q', \
             'area',  'vol',  'pres',  'jpol', \
            'darea', 'dvol', 'dpres', 'djpol') :
            if self.__dict__[key] is not None:
                self.__dict__[key+'_full'] = self.__dict__[key][self.indt, :]
                self.__dict__[key] = self.__dict__[key][self.indt, :nrho]

        ## Geometric major axis [m]
        self.R0 = 1.65
        ## Central magnetic field F/R [T]
        self.B0 = self.jpol[..., 0]*2e-7/self.R0
        ## Magnetic field on magnetic axxis [T]
        self.Baxis = self.jpol[..., 0]*2e-7/self.Rmag
        ## Normalised poloidal flux [Vs]
        self.psiN = (self.pfl             - self.psi0[..., None]) / \
                    (self.psix[..., None] - self.psi0[..., None])

        grad_area = np.apply_along_axis(np.gradient, -1, self.area)

        if self.ffp is not None and self.rinv is not None:
            self.jav = 2.*np.pi*self.dpres/self.rinv + self.ffp*self.rinv/2e-7
            curr_prof = np.cumsum(self.jav*grad_area, axis=-1)
        ## Plasma current [A] as integral of current density
            self.ip = curr_prof[..., -1]

        self.q2 = np.zeros_like(self.q)
        for jt in range(self.q.shape[0]):
            self.q2[jt,  :] = self.q[jt, :]
            self.q [jt, -1] = 2*self.q[jt, -2] - self.q[jt, -3]
            self.q2[jt, -1] = 1.25*self.q[jt, -1]
#            print(self.q2[jt, -1], self.q[jt, -1])


        ## Unnormalised rho toroidal
        self.rho_tor = np.sqrt(np.abs(self.tfl/(np.pi*self.B0[..., None])))
        ## Normalised rho toroidal
        self.rho_tor_n = np.zeros_like(self.tfl)
        self.rhotor_trapz = np.zeros_like(self.tfl) # for RABBIT
        ## Normalised toroidal flux [Vs]
        self.tfln = np.zeros_like(self.tfl)
        for jt in range(nt):
            tf = self.tfl[jt]
            torflux_trapz = cumtrapz(-self.q2[jt], x=self.pfl[jt], initial=0.)
            self.tfln[jt, :] = tf/tf[-1]
            self.rho_tor_n[jt, 1:] = np.sqrt((tf[1:] - tf[0])/(tf[-1] - tf[0]))
            self.rhotor_trapz[jt, 1:] = np.sqrt( torflux_trapz[1:] / (torflux_trapz[-1] - torflux_trapz[0]) )

        self.pfm = self.pfm[:, :, self.indt]


    def read_pfm(self):

        """
        Reads PFM matrix
        """

        nt = len(self.time)
        nR = len(self.Rmesh)
        nZ = len(self.Zmesh)
        ## Poloidal flux matrix [Vs]
        self.pfm = self.sf.getobject('PFM')[: nR, : nZ, :nt]


    def read_ssq(self):

        """
        Creating attributes corresponding to SSQNAM.
        Beware: in different shotfiles, for a given j0 
        SSQ[j0, time] can represent a different variable.
        This routine handles it consistently.
        """

        ssqs   = self.sf.getobject('SSQ') # Time is second
        ssqnam = self.sf.getobject('SSQnam')

        nt = len(self.time)
        ## Names of SSQ parameters
        self.ssqnames = []
        for jssq in range(ssqnam.shape[1]):
            lbl = ''.join(ssqnam[:, jssq]).strip()
            if lbl.strip():
                if lbl not in self.ssqnames: # avoid double names
                    self.ssqnames.append(lbl)
                    ## Scalar quantities
                    self.__dict__[lbl] = ssqs[jssq, :nt]


    def read_scalars(self):

        """
        Reads R, z, psi at magnetic axis and separatrix, only if attribute 'r0' is missing.
        equ_map.r0 is deleted at any equ_map.Open, equ_map.Close call.
        """

        self.read_ssq()

        nt = len(self.time)
# Position of mag axis, separatrixx

        self.PFxx = self.sf.getobject('PFxx')[:, :nt]
        ikCAT = np.argmin(abs(self.PFxx[1:, :] - self.PFxx[0, :]), axis=0) + 1
        if all(self.PFxx[2]) == 0: ikCAT[:] = 1  #troubles with TRE equilibrium 

        ## Poloidal flux at magnetic axis [Vs]
        self.psi0 = self.PFxx[0, :nt]
        ## Poloidal flux at separatrix [Vs]
        self.psix = self.PFxx[ikCAT, np.arange(nt)]

        try:
            ## Plasma current[A]
            self.ipipsi = self.sf.getobject('IpiPSI')[0]
        except:
            logger.exception('Signal IpiPSI not found')


    def read_profiles(self):
        """Reading 1D quantities, including some derivatives"""

        ## Toroidal flux(t, rho) [Vs]
        self.tfl = self.get_profile('TFLx')
        ## Poloidal flux (t, rho) [Vs]
        self.pfl = self.get_profile('PFL')
        ## Safety factor(t, rho)
        self.q     = self.get_profile('Qpsi')
        ## FF'
        self.ffp   = self.get_profile('FFP')
        self.rinv  = self.get_profile('Rinv')
        self.r2inv = self.get_profile('R2inv')
        self.bave  = self.get_profile('Bave')
        self.b2ave = self.get_profile('B2ave')

        ## dVolume/dPsi [m**3/Vs]
        self.vol , self.dvol  = self.get_mixed('Vol')
        ## dArea/dPsi [m**2/Vs]
        self.area, self.darea = self.get_mixed('Area')
        ## dPres/dPsi [Pa/Vs]
        self.pres, self.dpres = self.get_mixed('Pres')
        self.jpol, self.djpol = self.get_mixed('Jpol')


    def get_profile(self, var_name):

        """
        var_name: str
            name of the quantity, like
            Qpsi       q_value vs PFL
            Bave       <B>vac
            B2ave      <B^2>vac
            FFP        ff'
            Rinv       <1/R>
            R2inv      <1/R^2>
            FTRA       fraction of the trapped particles
        Output:
            array(t, rho) with some metadata (units, description)
        """

        nt = len(self.time)

        profs = ('TFLx', 'PFL', 'FFP', 'Qpsi', 'Rinv', 'R2inv', 'Bave', 'B2ave')

        if var_name not in profs:
            logger.error('SignalGroup %s unknown' %var_name)
            return None

        tmp = self.sf.getobject(var_name)
        if tmp is None:
            return None
        var = tmp[:, :nt]

        nrho = np.max(self.lpfp + 1 + self.lpfe)
        
        var_sorted = sfobj.SFOBJ(np.zeros((nt, nrho)), sfho=tmp)
        for jt in range(nt):
            sort_wh = self.ind_sort[jt]
            nr = len(sort_wh)
            var_sorted [jt, :nr] = var[sort_wh, jt]
            if nr < nrho:
                var_sorted[jt, nr:] = var_sorted[jt, nr-1]

        return var_sorted


    def get_mixed(self, var_name):

        """
        var_name: str
            name of the quantity, like
            Jpol       poloidal current,
            Pres       pressure
            Vol        plasma Volume
            Area       plasma Area
        Output:
            array-pair (quantity(t, rho), derivative(t, rho)) with some metadata (units, description)
        """

        nt = len(self.time)
        mixed = ('Vol', 'Area', 'Pres', 'Jpol')

# Pairs prof, d(prof)/d(psi)

        if var_name not in mixed:
            logger.error('%s not one of the mixed quanties Vol, Area, Pres, Jpol' %var_name)
            return None, None

        tmp = self.sf.getobject(var_name)
        var  = tmp[ ::2, :nt]
        dvar = tmp[1::2, :nt]

        nrho = np.max(self.lpfp + 1 + self.lpfe)
        info  = type('', (), {})()
        dinfo = type('', (), {})()
        for key, val in tmp.__dict__.items():
            if key != 'data':
                info.__dict__[key] = val
                if key == 'phys_unit':
                    dinfo.__dict__[key] = '%s/%s' %(val, self.pfl.phys_unit)
                else:
                    dinfo.__dict__[key] = val
        var_sorted  = sfobj.SFOBJ( np.zeros((nt, nrho)), sfho=info)
        dvar_sorted = sfobj.SFOBJ( np.zeros((nt, nrho)), sfho=dinfo)
        for jt in range(nt):
            sort_wh = self.ind_sort[jt]
            nr = len(sort_wh)
            var_sorted [jt, :nr] = var [sort_wh, jt]
            dvar_sorted[jt, :nr] = dvar[sort_wh, jt]
            if nr < nrho:
                var_sorted [jt, nr:] = var_sorted[jt, nr-1]

        return var_sorted, dvar_sorted


    def B_mesh(self):

        """calculates Br, Bz, Bt profiles
         """

        nt = len(self.time)

# Poloidal current 

        nr = len(self.Rmesh)
        nz = len(self.Zmesh)
        dr = self.Rmesh[1] - self.Rmesh[0]
        dz = self.Zmesh[1] - self.Zmesh[0]

        self.Br = np.zeros((nt, nr, nz), dtype=np.float32)
        self.Bz = np.zeros_like(self.Br)
        self.Bt = np.zeros_like(self.Br)

        for jt in range(nt):
            Psi = self.pfm[:, :, jt]
# Eq 12 in Coco paper
            Bpol = np.gradient(Psi, dr, dz)/self.Rmesh[:, None]
            self.Br[jt] =  Bpol[1]
            self.Bz[jt] = -Bpol[0]
            fBt = interp1d(self.pfl[jt], self.jpol[jt], kind='linear', fill_value='extrapolate')
            self.Bt[jt] = fBt(Psi)*mu_0/self.Rmesh[:, None]

        self.Br /= -abs(self.psi_fac)
        self.Bz /= -abs(self.psi_fac)
        self.Bt /= 2.*np.pi


    def find_coco(self, ip_shot='ccw', bt_shot='cw'):
        """
        Identifies the COCO number of a given equilibrium object
        """

# dpsi_sign positive if psi_sep > psi0
        dpsi_sign = np.sign(np.mean(self.psix) - np.mean(self.psi0))
# Known plasma discharge
        ccw_ip = 1 if(ip_shot == 'ccw') else -1 # AUG default: 1
        ccw_bt = 1 if(bt_shot == 'ccw') else -1 # AUG default: -1

# Table III

        sign_q  = np.sign(np.nanmean(self.q))
        sign_ip = np.sign(np.nanmean(self.ipipsi))
        sign_bt = np.sign(np.nanmean(self.jpol))
        sigma_rphiz = sign_ip*ccw_ip
        sigma_bp    = dpsi_sign*sign_ip
# Eq 45
        sigma_rhothephi = sign_q*sign_ip*sign_bt
        logger.debug(sigma_bp, sigma_rphiz, sigma_rhothephi)
        for jc, rhothephi in enumerate(sigma['rhothephi']):
            if(sigma['bp'   ][jc] == sigma_bp    and \
               sigma['rphiz'][jc] == sigma_rphiz and \
               rhothephi          == sigma_rhothephi):
                self.cocos = jc + 1
                break

# Find out 2*pi factor for Psi

        dphi = np.gradient(self.tfl, axis=1)
        dpsi = np.gradient(self.pfl, axis=1)

# Radial+time average
# It is either q_ratio ~ 1 (COCO > 10) or ~ 2*pi (COCO < 10)
        q_ratio = np.abs(np.nanmean(dphi/(self.q*dpsi)))
        logger.debug('Ratio %8.4f' %q_ratio)
        if q_ratio < 4:
            self.cocos += 10


    def to_coco(self, cocos_out=11):
        """
        Transforms equilibrium object into any wished output COCO
        """

# Assuming SI

        cocos_in = self.cocos
        logger.info('COCO conversion from %d to %d' %(cocos_in, cocos_out))
        jc_in   = cocos_in %10 - 1
        jc_out  = cocos_out%10 - 1
        ebp_in  = cocos_in//10
        ebp_out = cocos_out//10
#    sign_ip_in = np.sign(np.nanmean(self.ipipsi))
# Equation 9, table I, equation 39, 45
        q_sign   = sigma['rhothephi'][jc_in]*sigma['rhothephi'][jc_out]
        phi_sign = sigma['rphiz'][jc_in]*sigma['rphiz'][jc_out]
        psi_sign = sigma['rphiz'][jc_in]*sigma['bp'][jc_in] * sigma['rphiz'][jc_out]*sigma['bp'][jc_out]
        psi_2pi  = (2.*np.pi)**(ebp_out - ebp_in)
        psi_fac = psi_sign*psi_2pi
        try:
            logger.debug(np.mean(self.jav), phi_sign)
        except:
            pass

        for key, val in self.__dict__.items():
            if val is None:
                continue
            if key in ('B0', 'Bt', 'Br', 'Bz', 'jpol', 'jav', 'tfl', 'ip', 'ipipsi', 'phi_sign'):
                self.__dict__[key] = val*phi_sign
            elif key in ('psi0', 'psix', 'pfl', 'pfm', 'psi_fac'):
                self.__dict__[key] = val*psi_fac
            elif key in ('dpres', 'darea', 'dvol', 'ffp'):
                self.__dict__[key] = val/psi_fac
            elif key in ('djpol', ):
                self.__dict__[key] = val*phi_sign/psi_fac
            elif key in ('q', 'q0', 'q25', 'q50', 'q75', 'q95'):
                self.__dict__[key] = val*q_sign
        self.cocos = cocos_out


    def timeDownsample(self, time_ds, noELMs=False, dt_out=None):

        indbin  = None # Compute first time
        ind_elm = None # Compute first time
        self.noELMs = noELMs
        nt = len(self.time)
        self.pfm, self.ind_elm, self.indbin = time_slice.map2tgrid(time_ds, self.time, np.transpose(self.pfm, axes=(2, 0, 1)), nshot=self.shot, noELMs=self.noELMs, dt_out=dt_out)
        self.pfm = np.transpose(self.pfm, axes=(1, 2, 0))

        for attr, val in self.__dict__.items():
            if attr in ('time', 'pfm'):
                continue
            if hasattr(val, 'shape'):
                if val.dtype not in (np.float16, np.float32, np.float64, '>f4'):
                    continue
                if val.ndim > 0:
                    if val.shape[0] == nt:
                        tmp, _, _ = time_slice.map2tgrid(time_ds, self.time, getattr(self, attr), ind_elm=ind_elm, indbin=indbin, dt_out=dt_out)
                        setattr(self, attr, tmp)

        self.time = time_ds

if __name__ == '__main__':


    nshot = 28053
    eqm = EQU(nshot)
    logger.info(eqm.ssqnames)
