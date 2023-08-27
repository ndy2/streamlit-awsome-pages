from python.auth import jwt_service
from python.auth.authenticator import Authenticator
from python.auth.domain import UserSource, User

app_user_source = UserSource()
app_user_source.add(User("haha", "haha", 27))
app_user_source.add(User("papa", "papa", 28))

app_authenticator = Authenticator(
    app_user_source,
    jwt_service
)
