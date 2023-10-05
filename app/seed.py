from app import app
from models import db, User, Product, Review, HairService, NailService, MakeupService, Appointment
from datetime import datetime, time



with app.app_context():
    Product.query.delete()
    User.query.delete()
    Review.query.delete()
    
    product1 = Product(
        name='Lip gloss',
        description='Rich gloss. It can be worn alone or on top of a nude or any other lipstick',
        image='https://images.unsplash.com/photo-1631214524115-9942bf927d4a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80',
        price=12.99,
    )

    product2 = Product(
        name='Eyeshadow Palette',
        description='A versatile eyeshadow palette with various shades for different eye looks',
        image='https://images.unsplash.com/photo-1614739846939-d50eefc99efc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&h=800&q=80',
        price=24.99,
    )

    product3 = Product(
        name='Mascara',
        description='Lengthening and volumizing mascara for bold, beautiful lashes',
        image='https://images.unsplash.com/photo-1631214499943-07647378b067?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1325&q=80',
        price=9.99,
    )

    product4 = Product(
        name='Foundation',
        description='A high-coverage foundation for a flawless complexion',
        image='https://images.unsplash.com/photo-1627885793933-584e53987c14?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1336&q=80',
        price=19.99,
    )
    
    
    user1 = User(
        username='Moses Chengo',
        email='moses@example.com',
        password='password123',
        phone_number = '0799863031'
    )

    user2 = User(
        username='Jane Smith',
        email='jane@example.com',
        password='secret',
        phone_number = '0790902345'
        
    )

    db.session.add_all([user1, user2])
    
    review1 = Review(review_text='They are awesome!', user=user1, rating=4.5)
    review2 = Review(review_text='The best beauty products i have ever seen!', user=user2, rating=5)
        
    hair_service1 = HairService(title='Haircut', description='Standard haircut', price=25.0)
    hair_service2 = HairService(title='Hair Color', description='Full hair coloring', price=60.0)

    nail_service1 = NailService(title='Manicure', description='Basic manicure', price=20.0)
    nail_service2 = NailService(title='Pedicure', description='Basic pedicure', price=25.0)

    makeup_service1 = MakeupService(title='Makeup Application', description='Professional makeup application', price=45.0)
    makeup_service2 = MakeupService(title='Bridal Makeup', description='Makeup for brides', price=90.0)

    appointment1 = Appointment(date=datetime(2023, 10, 10), time=time(10, 0), service='Haircut', extra_information='No specific instructions', user=user1)
    appointment2 = Appointment(date=datetime(2023, 8, 12), time=time(12,30), service='Manicure', extra_information='French manicure', user=user2)

    db.session.add_all([product1, product2, product3, product4, user1, user2, review1, review2 ,hair_service1, hair_service2, nail_service1, nail_service2, makeup_service1, makeup_service2, appointment1, appointment2])
    db.session.commit()


    db.session.commit()