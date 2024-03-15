import datetime
import uuid


class Session:
    def __init__(self, id: str, username: str, timeout: datetime.datetime):
        self.id = id
        self.username = username
        self.timeout = timeout

    @staticmethod
    def create_session(username: str):
        return Session(
            id=str(uuid.uuid4()),
            username=username,
            timeout=datetime.datetime.now() + datetime.timedelta(hours=1),
        )

    def check_timeout(self) -> bool:
        return datetime.datetime.now() < self.timeout


class SessionPool:
    def __init__(self):
        self.sessions = []

    def create_session(self, username: str) -> str:
        session = Session.create_session(username)
        self.sessions.append(session)
        return session.id

    def remove_session(self, session_id: str):
        session = self.get_session_by_id(session_id)
        if session is not None:
            self.sessions.remove(session)

    def get_session_by_id(self, session_id: str) -> Session | None:
        for session in self.sessions:
            if session.id == session_id:
                return session
        return None

    def get_session_by_username(self, username: str) -> Session | None:
        for session in self.sessions:
            if session.username == username:
                return session
        return None
