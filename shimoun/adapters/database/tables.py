from video_markup.adapters.database.base import Base, IdentifableMixin, TimestampedMixin


class Users(IdentifableMixin, TimestampedMixin, Base):
    __tablename__ = "users"