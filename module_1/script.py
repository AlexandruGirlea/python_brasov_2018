import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-n", "--name", required=False,	help="name of the user")

args = vars(ap.parse_args())

if args['name']:
    print(args['name'], 'is the best programmer')

else:
    print('I am a good programmer')
