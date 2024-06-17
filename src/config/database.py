import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_username = "root"
db_password = "PuigKcStMFGje584"
db_url = "services.irn6.chabokan.net:46763"
db_name = "nigel"
DATABASE_URL = f'mysql+mysqlconnector://{db_username}:{db_password}@{db_url}/{db_name}?charset=utf8mb4'

# Retrieve database credentials from environment variables
# DATABASE_URL = os.getenv("PLATFORM_RELATIONSHIPS")
# if DATABASE_URL:
#     import json
#     relationships = json.loads(DATABASE_URL)
#     database = relationships['database'][0]
#     user = database['username']
#     password = database['password']
#     host = database['host']
#     database_name = database['path']
#     DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}/{database_name}"

# use echo=True for debugging
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()