from sqlalchemy import Integer, String, Text, Boolean, DateTime, null, text
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(String(36), primary_key=True, default=text('UUID()'))
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=text('NOW()'))
    updated_at = Column(DateTime, onupdate=text('NOW()'))

    user = relationship('User', back_populates='tasks')
