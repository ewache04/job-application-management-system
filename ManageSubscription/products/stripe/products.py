# ManageSubscription/products/products.py
def products_type(name=None, price=None, currency='USD', description=None):
    # Define the products with features
    return [
        {
            'name': name or 'SUBSCRIPTION',
            'price': price or 29,
            'currency': currency,
            'interval': 'mo',
            'description': description or 'Default subscription description',
            'features': [
                'Store Resume',
                'Track Progress',
                'Password Storage',
                'Track Applications',
                'Communication Storage',
                'Automated Cover Letter',
                'Automated Follow-up message',

            ],
        },
    ]
