from faker import Faker

from app import app

from models import User, Product,Order

with app.app_context():
    fake = Faker()

    Product.query.delete()
    products=[
        Product(name="Lotion", price="750", description=fake.sentence()),
        Product(name="Mosturizer", price="750", description=fake.sentence()),
        Product(name="Make-up Brush", price="750", description=fake.sentence()),
        Product(name="Foundation", price="750", description=fake.sentence()),
        Product(name="Nail Polish", price="750", description=fake.sentence()),
        Product(name="Gel", price="750", description=fake.sentence()),
        Product(name="Lipstick", price="750", description=fake.sentence()),
        Product(name="Cream", price="750", description=fake.sentence()),
        Product(name="Perfume", price="750", description=fake.sentence()),
        Product(name="Sunscreen", price="750", description=fake.sentence()),
        Product(name="Eyeshadow", price="750", description=fake.sentence()),
        Product(name="Concealer", price="750", description=fake.sentence()),
        Product(name="Blush", price="750", description=fake.sentence()),
        Product(name="Mascara", price="750", description=fake.sentence()),
        Product(name="", price="750", description=fake.sentence()),
        Product(name="Lotion", price="750", description=fake.sentence())

    ]
















































    # for p in range(70):
    #     # fake_image = fake.jpeg_file()
    #     product = Product(
    #         name=fake.word(),
    #         price=fake.random_int(0, 4000),
    #         description=fake.sentence(),
    #         # image=str(fake_image)
    #     )
    #     products.append(product)