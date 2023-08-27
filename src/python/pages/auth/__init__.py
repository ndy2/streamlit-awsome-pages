import extra_streamlit_components as stx

from python.auth.authenticator import Authenticator
from python.auth.domain import UserSource, User
from python.auth.support import JwtService
from python.auth.support import SessionManager

app_user_source = UserSource()
app_user_source.add(User("haha", "haha", 27))
app_user_source.add(User("papa", "papa", 28))

app_authenticator = Authenticator(
    app_user_source,
    JwtService(),
    stx.CookieManager(),
    SessionManager()
)
