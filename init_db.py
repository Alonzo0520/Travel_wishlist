from app import app, db, User, Destination

def init_database():
    with app.app_context():
        # Create all tables
        db.create_all()

if __name__ == '__main__':
    init_database()
    print("Database tables created.")
