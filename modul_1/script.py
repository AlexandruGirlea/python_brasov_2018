import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--name", required=False,	help="name of the user")

args = vars(ap.parse_args())

if args['name']:
    print(args['name'], 'este cel mai bun programator')

else:
    print('Sunt un programator bun')
