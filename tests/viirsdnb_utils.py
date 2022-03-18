# flake8: noqa
from collections import namedtuple

import responses  # type: ignore

MockLink = namedtuple("MockLink", "url html_content method")

mines_login_form = {
    "monthly_vcmslcfg": MockLink(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg/SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz",
        """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" class="login-pf">

<head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="robots" content="noindex, nofollow">

            <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>Log in to Earth Observation Group Login</title>
    <link rel="icon" href="/auth/resources/afx5f/login/eog/img/favicon.ico" />
            <link href="/auth/resources/afx5f/common/keycloak/node_modules/patternfly/dist/css/patternfly.min.css" rel="stylesheet" />
            <link href="/auth/resources/afx5f/common/keycloak/node_modules/patternfly/dist/css/patternfly-additions.min.css" rel="stylesheet" />
            <link href="/auth/resources/afx5f/common/keycloak/lib/zocial/zocial.css" rel="stylesheet" />
            <link href="/auth/resources/afx5f/login/eog/css/login.css" rel="stylesheet" />
</head>

<body class="">
  <div class="login-pf-page">
    <div id="kc-header" class="login-pf-page-header">
      <div id="kc-header-wrapper" class=""><div class="kc-logo-text"><span>EOG</span></div></div>
    </div>
    <div class="card-pf ">
      <header class="login-pf-header">
            <div id="kc-locale">
                <div id="kc-locale-wrapper" class="">
                    <div class="kc-dropdown" id="kc-locale-dropdown">
                        <a href="#" id="kc-current-locale-link">English</a>
                        <ul>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=de">Deutsch</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=no">Norsk</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=ru">Русский</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=sv">Svenska</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=pt-BR">Português (Brasil)</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=lt">Lietuvių</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=en">English</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=it">Italiano</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=fr">Français</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=zh-CN">中文简体</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=es">Español</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=cs">Čeština</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=ja">日本語</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=sk">Slovenčina</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=pl">Polish</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=ca">Català</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=nl">Nederlands</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&kc_locale=tr">tr</a></li>
                        </ul>
                    </div>
                </div>
            </div>
                <h1 id="kc-page-title">        Log In

</h1>
      </header>
      <div id="kc-content">
        <div id="kc-content-wrapper">


    <div id="kc-form" >
      <div id="kc-form-wrapper" >
            <form id="kc-form-login" onsubmit="login.disabled = true; return true;" action="https://eogauth.mines.edu/auth/realms/master/login-actions/authenticate?session_code=YeRo9eN7i3k6H-qVN9NQRneZNxi89c1quseqzJmGggE&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg" method="post">
                <div class="form-group">
                    <label for="username" class="control-label">Email</label>

                        <input tabindex="1" id="username" class="form-control" name="username" value=""  type="text" autofocus autocomplete="off" />
                </div>

                <div class="form-group">
                    <label for="password" class="control-label">Password</label>
                    <input tabindex="2" id="password" class="form-control" name="password" type="password" autocomplete="off" />
                </div>

                <div class="form-group login-pf-settings">
                    <div id="kc-form-options">
                            <div class="checkbox">
                                <label>
                                        <input tabindex="3" id="rememberMe" name="rememberMe" type="checkbox"> Remember me
                                </label>
                            </div>
                        </div>
                        <div class="">
                                <span><a tabindex="5" href="/auth/realms/master/login-actions/reset-credentials?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg">Forgot Password?</a></span>
                        </div>

                  </div>

                  <div id="kc-form-buttons" class="form-group">
                      <input type="hidden" id="id-hidden-input" name="credentialId" />
                      <input tabindex="4" class="btn btn-primary btn-block btn-lg" name="login" id="kc-login" type="submit" value="Log In"/>
                  </div>
            </form>
        </div>
      </div>



              <div id="kc-info" class="login-pf-signup">
                  <div id="kc-info-wrapper" class="">
            <div id="kc-registration">
                <span>New user? <a tabindex="6" href="/auth/realms/master/login-actions/registration?client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg">Register</a></span>
            </div>

                  </div>
              </div>
        </div>
      </div>

    </div>
  </div>
</body>
</html>
""",
        responses.GET,
    ),
    "monthly_vcmcfg": MockLink(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmcfg/SVDNB_npp_19000901-19000930_00N060E_vcmcfg_v10_c190010112300.tgz",
        """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" class="login-pf">

<head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="robots" content="noindex, nofollow">

            <meta name="viewport" content="width=device-width,initial-scale=1"/>
    <title>Log in to Earth Observation Group Login</title>
    <link rel="icon" href="/auth/resources/afx5f/login/eog/img/favicon.ico" />
            <link href="/auth/resources/afx5f/common/keycloak/node_modules/patternfly/dist/css/patternfly.min.css" rel="stylesheet" />
            <link href="/auth/resources/afx5f/common/keycloak/node_modules/patternfly/dist/css/patternfly-additions.min.css" rel="stylesheet" />
            <link href="/auth/resources/afx5f/common/keycloak/lib/zocial/zocial.css" rel="stylesheet" />
            <link href="/auth/resources/afx5f/login/eog/css/login.css" rel="stylesheet" />
</head>

<body class="">
  <div class="login-pf-page">
    <div id="kc-header" class="login-pf-page-header">
      <div id="kc-header-wrapper" class=""><div class="kc-logo-text"><span>EOG</span></div></div>
    </div>
    <div class="card-pf ">
      <header class="login-pf-header">
            <div id="kc-locale">
                <div id="kc-locale-wrapper" class="">
                    <div class="kc-dropdown" id="kc-locale-dropdown">
                        <a href="#" id="kc-current-locale-link">English</a>
                        <ul>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=de">Deutsch</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=no">Norsk</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=ru">Русский</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=sv">Svenska</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=pt-BR">Português (Brasil)</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=lt">Lietuvių</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=en">English</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=it">Italiano</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=fr">Français</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=zh-CN">中文简体</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=es">Español</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=cs">Čeština</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=ja">日本語</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=sk">Slovenčina</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=pl">Polish</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=ca">Català</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=nl">Nederlands</a></li>
                                <li class="kc-dropdown-item"><a href="/auth/realms/master/login-actions/authenticate?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;kc_locale=tr">tr</a></li>
                        </ul>
                    </div>
                </div>
            </div>
                <h1 id="kc-page-title">        Log In

</h1>
      </header>
      <div id="kc-content">
        <div id="kc-content-wrapper">


    <div id="kc-form" >
      <div id="kc-form-wrapper" >
            <form id="kc-form-login" onsubmit="login.disabled = true; return true;" action="https://eogauth.mines.edu/auth/realms/master/login-actions/authenticate?session_code=OHHYRdMyNESqUCaF6KWhvUUjfNwcYpNUeRl_lfxm6S0&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&amp;client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4" method="post">
                <div class="form-group">
                    <label for="username" class="control-label">Email</label>

                        <input tabindex="1" id="username" class="form-control" name="username" value=""  type="text" autofocus autocomplete="off" />
                </div>

                <div class="form-group">
                    <label for="password" class="control-label">Password</label>
                    <input tabindex="2" id="password" class="form-control" name="password" type="password" autocomplete="off" />
                </div>

                <div class="form-group login-pf-settings">
                    <div id="kc-form-options">
                            <div class="checkbox">
                                <label>
                                        <input tabindex="3" id="rememberMe" name="rememberMe" type="checkbox"> Remember me
                                </label>
                            </div>
                        </div>
                        <div class="">
                                <span><a tabindex="5" href="/auth/realms/master/login-actions/reset-credentials?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4">Forgot Password?</a></span>
                        </div>

                  </div>

                  <div id="kc-form-buttons" class="form-group">
                      <input type="hidden" id="id-hidden-input" name="credentialId" />
                      <input tabindex="4" class="btn btn-primary btn-block btn-lg" name="login" id="kc-login" type="submit" value="Log In"/>
                  </div>
            </form>
        </div>
      </div>



              <div id="kc-info" class="login-pf-signup">
                  <div id="kc-info-wrapper" class="">
            <div id="kc-registration">
                <span>New user? <a tabindex="6" href="/auth/realms/master/login-actions/registration?client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4">Register</a></span>
            </div>

                  </div>
              </div>
        </div>
      </div>

    </div>
  </div>
</body>
</html>
        """,
        responses.GET,
    ),
}

mines_login_form_post = {
    "monthly_vcmslcfg": MockLink(
        "https://eogauth.mines.edu/auth/realms/master/login-actions/authenticate?session_code="
        + "YeRo9eN7i3k6H-qVN9NQRneZNxi89c1quseqzJmGggE&execution=c7533e04-71c8-4262-9c0e-29c77ac47521&"
        + "client_id=eogdata_oidc&tab_id=Wbk6_AZ6_Xg",
        "",
        responses.POST,
    ),
    "monthly_vcmcfg": MockLink(
        "https://eogauth.mines.edu/auth/realms/master/login-actions/authenticate?session_code="
        + "OHHYRdMyNESqUCaF6KWhvUUjfNwcYpNUeRl_lfxm6S0&amp;execution=c7533e04-71c8-4262-9c0e-29c77ac47521&"
        + "amp;client_id=eogdata_oidc&amp;tab_id=uBYGaKPknp4",
        "",
        responses.POST,
    ),
}

mines_dir_listing = {
    "monthly_vcmslcfg": MockLink(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmslcfg",
        """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Index of /nighttime_light/monthly/v10/1900/190009/vcmslcfg</title>
    <link rel="stylesheet" href="/wwwdata/viirs_products/dnb_composites/theme/style.css" type="text/css"/>
    <link rel="shortcut icon" href="/wwwdata/viirs_products/dnb_composites/theme/favicon.ico"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
<body>
    <div class="wrapper">
        <!-- we open the `wrapper` element here, but close it in the `footer.html` file -->

        <ol class="breadcrumb" id="breadcrumb"></ol>

        <input type="search" id="filter" placeholder="filter contents"/>


        EOG Nighttime Light
        <!--{HEADER-MESSAGE}-->
        <table id="indexlist">
            <tr class="indexhead">
                <th class="indexcolicon">
                    <img src="/wwwdata/viirs_products/dnb_composites/theme/icons/blank.png" alt="[ICO]"/>
                </th>
                <th class="indexcolname">
                    <a href="?C=N;O=D">Name</a>
                </th>
                <th class="indexcollastmod">
                    <a href="?C=M;O=A">Last modified</a>
                </th>
                <th class="indexcolsize">
                    <a href="?C=S;O=A">Size</a>
                </th>
            </tr>
            <tr class="even">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_00N060E_vcmslcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:19  </td>
                <td class="indexcolsize">532M</td>
            </tr>
            <tr class="odd">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_00N060W_vcmslcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_00N060W_vcmslcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_00N060W_vcmslcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:19  </td>
                <td class="indexcolsize">516M</td>
            </tr>
            <tr class="even">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_00N180W_vcmslcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_00N180W_vcmslcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_00N180W_vcmslcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:19  </td>
                <td class="indexcolsize">519M</td>
            </tr>
            <tr class="odd">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_75N060E_vcmslcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_75N060E_vcmslcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_75N060E_vcmslcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:19  </td>
                <td class="indexcolsize">590M</td>
            </tr>
            <tr class="even">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_75N060W_vcmslcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_75N060W_vcmslcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_75N060W_vcmslcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:19  </td>
                <td class="indexcolsize">605M</td>
            </tr>
            <tr class="odd">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_75N180W_vcmslcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_75N180W_vcmslcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_75N180W_vcmslcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:19  </td>
                <td class="indexcolsize">624M</td>
            </tr>
        </table>
        <div class="block">
            <!--{FOOTER-MESSAGE}-->

        </div>
        <!--/.postlisting-->

    </div>
    <!--/.wrapper-->

    <div class="footer">
      Apaxy by @adamwhitcroft
    </div>
    <!--/.footer-->
    <script src=/wwwdata/viirs_products/dnb_composites//theme/apaxy.js></script>
</body>
</html>
    """,
        responses.GET,
    ),
    "monthly_vcmcfg": MockLink(
        "https://eogdata.mines.edu/nighttime_light/monthly/v10/1900/190009/vcmcfg",
        """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Index of /nighttime_light/monthly/v10/1900/190009/vcmcfg</title>
    <link rel="stylesheet" href="/wwwdata/viirs_products/dnb_composites/theme/style.css" type="text/css"/>
    <link rel="shortcut icon" href="/wwwdata/viirs_products/dnb_composites/theme/favicon.ico"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
</head>
<body>
    <div class="wrapper">
        <!-- we open the `wrapper` element here, but close it in the `footer.html` file -->

        <ol class="breadcrumb" id="breadcrumb"></ol>

        <input type="search" id="filter" placeholder="filter contents"/>


        EOG Nighttime Light
        <!--{HEADER-MESSAGE}-->
        <table id="indexlist">
            <tr class="indexhead">
                <th class="indexcolicon">
                    <img src="/wwwdata/viirs_products/dnb_composites/theme/icons/blank.png" alt="[ICO]"/>
                </th>
                <th class="indexcolname">
                    <a href="?C=N;O=D">Name</a>
                </th>
                <th class="indexcollastmod">
                    <a href="?C=M;O=A">Last modified</a>
                </th>
                <th class="indexcolsize">
                    <a href="?C=S;O=A">Size</a>
                </th>
            </tr>
            <tr class="even">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_00N060E_vcmcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_00N060E_vcmcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_00N060E_vcmcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:18  </td>
                <td class="indexcolsize">523M</td>
            </tr>
            <tr class="odd">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_00N060W_vcmcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_00N060W_vcmcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_00N060W_vcmcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:18  </td>
                <td class="indexcolsize">510M</td>
            </tr>
            <tr class="even">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_00N180W_vcmcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_00N180W_vcmcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_00N180W_vcmcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:18  </td>
                <td class="indexcolsize">508M</td>
            </tr>
            <tr class="odd">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_75N060E_vcmcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_75N060E_vcmcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_75N060E_vcmcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:18  </td>
                <td class="indexcolsize">407M</td>
            </tr>
            <tr class="even">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_75N060W_vcmcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_75N060W_vcmcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_75N060W_vcmcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:18  </td>
                <td class="indexcolsize">413M</td>
            </tr>
            <tr class="odd">
                <td class="indexcolicon">
                    <a href="SVDNB_npp_19000901-19000930_75N180W_vcmcfg_v10_c190010112300.tgz">
                        <img src="/icons/compressed.gif" alt="[   ]"/>
                    </a>
                </td>
                <td class="indexcolname">
                    <a href="SVDNB_npp_19000901-19000930_75N180W_vcmcfg_v10_c190010112300.tgz">SVDNB_npp_19000901-19000930_75N180W_vcmcfg_v10_c190010112300.tgz</a>
                </td>
                <td class="indexcollastmod">2022-01-05 04:18  </td>
                <td class="indexcolsize">422M</td>
            </tr>
        </table>
        <div class="block">
            <!--{FOOTER-MESSAGE}-->

        </div>
        <!--/.postlisting-->

    </div>
    <!--/.wrapper-->

    <div class="footer">
      Apaxy by @adamwhitcroft
    </div>
    <!--/.footer-->
    <script src=/wwwdata/viirs_products/dnb_composites//theme/apaxy.js></script>
</body>
</html>
""",
        responses.GET,
    ),
}
