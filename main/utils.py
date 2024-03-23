
def user_listing_directory_path(instance, filename):
    return 'user_{0}/listings/{1}'.format(instance.seller.users.id, filename)