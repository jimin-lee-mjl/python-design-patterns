from factories.concrete_item_factory import JeanFactory,HoodieFactory
from factories.abstract_clothes_factory import DeveloperSetupFactory


hoodie = HoodieFactory.create_object('lg')
jean = JeanFactory.create_object('md')
print(f'Hoodie: {hoodie.get_size()}, Jean: {jean.get_size()}')

developer_hoodie, developer_jean = DeveloperSetupFactory.get_setup(['lg', 'md'])
print(f'Hoodie: {developer_hoodie.get_size()}, Jean: {developer_jean.get_size()}')
