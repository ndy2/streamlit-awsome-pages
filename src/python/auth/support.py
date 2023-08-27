from typing import Any

import jwt
import streamlit as st


class JwtService:
    key = "key"
    algorithm = "HS256"

    def encode(self, payload: dict[str, Any]) -> str:
        return jwt.encode(payload, self.key, self.algorithm)

    def decode(self, token) -> dict[str, Any]:
        return jwt.decode(token, self.key, self.algorithm)


class SessionManager:

    def get(self, key: str) -> Any:
        return st.session_state[key]

    def set(self, key: str, value: Any) -> None:
        st.session_state[key] = value

    def set_if_none(self, key: str, value: Any) -> None:
        if key not in st.session_state:
            st.session_state[key] = value
