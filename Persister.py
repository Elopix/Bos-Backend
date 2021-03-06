import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker, scoped_session
import Database
from Database import User

tableName = 'bos-db'
userName = 'root'
password = ''

conn = sqla.create_engine('mysql+pymysql://' + userName + ':' + password + '@localhost/' + tableName + '?charset=utf8')
Session = scoped_session(sessionmaker(bind=conn))
class Persister:
	def __init__(self):
		print("creating perister")

	def storeObject(self, object):
		db = Session()
		try:
			db.add(object)
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True

	def deleteObject(self, object):
		db = Session()
		try:
			db.delete(object)
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True
	
	#gets a user object by id, returns user object or False
	def getUserById(self, id):
		db = Session()
		user = db.query(User).filter(User.id == id).first()
		db.close()
		if user is not None:
			return user
		return False

	#gets a user object by email, returns user object or False
	def getUserByEmail(self, email):
		db = Session()
		user = db.query(User).filter(User.email == email.lower()).first()
		db.close()
		if user is not None:
			return user
		return False

	#sets a user's authenticated field in db on True to indicate that the user is logged in
	def setAuthenticated(self, email):
		db = Session()
		try:
			user = db.query(User).filter(User.email == email.lower()).first()
			user.authenticated = True
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True

	def setNotAuthenticated(self, email):
		db = Session()
		try:
			user = db.query(User).filter(User.email == email.lower()).first()
			user.authenticated = False
			db.commit()
		except:
			db.close()
			return False
		db.close()
		return True