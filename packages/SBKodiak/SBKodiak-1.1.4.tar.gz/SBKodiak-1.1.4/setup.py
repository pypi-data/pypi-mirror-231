from setuptools import setup

setup(name='SBKodiak',
      version='1.1.4',
      description='SanBlaze Python control of Kodiak Modules',
      author='Matt Holsey',
      author_email='mholsey@sanblaze.com',
      url='https://www.sanblaze.com/',
      license='SanBlaze Technology ltd',
      packages=['SBKodiak', 
				'SBKodiak.docs',
				'SBKodiak.tests'],
	  install_requires=[
			    'paramiko',
			    'requests',
				'urllib3',
		  ],
      include_package_data=True,
      zip_safe=False)