import connexion

from connexion.resolver import RestyResolver


if __name__ == '__main__':
	app = connexion.App(__name__, 9090, specification_dir='swagger/')
	app.add_api('my_super_apps.yaml', resolver=RestyResolver('api'))
	app.run()
