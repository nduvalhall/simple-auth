from .database import session_pool, user_pool


def register_user(username: str, password: str) -> str:
    user_pool.add_user(username, password)
    return session_pool.create_session(username)


def delete_user(username: str):
    user_pool.remove_user(username)


def login_password(username: str, password: str) -> str:
    session = session_pool.get_session_by_username(username)

    if session is not None:
        return session.id

    user = user_pool.get_user(username)

    if user is None:
        raise ValueError("User not found")

    if not user.check_password(password):
        raise ValueError("Invalid password")

    return session_pool.create_session(username)


def login_session(session_id: str) -> str:
    session = session_pool.get_session_by_id(session_id)

    if session is None:
        raise ValueError("Invalid session")

    if not session.check_timeout():
        raise ValueError("Session timeout")

    return session.username


def logout_session(session_id: str):
    session_pool.remove_session(session_id)
