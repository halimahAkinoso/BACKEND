from sqlalchemmy import create_engine, text
# from sqlalchemmy import text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os
load_dotenv 


# db_url-dialect+driver:dbpassword:dbhost:dbport:dbname
# establishing connection to our database
db_url-f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"

engine = create_engine(
    db_url,
    connect_args={"client_flag": CLIENT.MULTI_STATEMENT}
    )

session = sessionmaker(bind=engine)

db = session()

# query=text("select * from user")

create_users = text("""
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL, 
    email VARCHAR (100) NOT NULL
);
""")
create_courses =text ("""
CREATE TABLE IF NOT EXISTS courses(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    level VARCHAR(100) NOT NULL
);
""")
create_courses =text ("""
CREATE TABLE IF NOT EXISTS enrollments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT,
    courseId INT,
    FOREIGN KEY (userId) REFERENCE users(id),
    FOREIGN KEY (courseId) REFERENCE  courses(id)
);
""")

db.execute(create_users)
db.execute(create_courses)
db.execute(create_enrollments)
print("Tables has been created successfully")