from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .Base import DeclarativeBase


class Tag(DeclarativeBase):

	# --------------------------------------------------------------------------
	# Schema configuration
	# --------------------------------------------------------------------------

	__tablename__ = 'Tag'

	# define table contents
	tag_text = Column(String(100), primary_key=True)
