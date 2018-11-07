import connexion

from connexion.resolver import RestyResolver


if __name__ == '__main__':
	apps = connexion.App(__name__, 9090, specification_dir='swagger/')
	apps.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
	apps.run()
