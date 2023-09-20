from copy import deepcopy
from hak.directory.empty import f as empty_directory
from hak.other.pip.dist_tar.make import f as make_new_dist_tar
from hak.other.pip.upload import f as start_upload
from hak.other.pip.version.get import f as get_pip_version
from hak.other.setup.cfg.update import f as update_setup_cfg
from hak.other.setup.py.update import f as update_setup_py

def f(x):
  x = deepcopy(x)
  z = {}
  z['v'] = x['v'] if 'v' in x else None
  z['root'] = x['root'] if 'root' in x else '.'
  z['cfg_path'] = f'{z["root"]}/setup.cfg'
  z['py_path'] = f'{z["root"]}/setup.py'

  z['v'] = z['v'] or get_pip_version('xgu')
  z['v']['patch'] += 1

  update_setup_cfg({'v': z['v'], 'filename': z['cfg_path']})
  update_setup_py({'v': z['v'], 'filename': z['py_path']})
  empty_directory('./dist/')
  
  make_new_dist_tar(x)
  # add_to_git(cwd=_root, cap_out=True)
  if 'local_test_only' not in x: z['upload_result'] = start_upload(x)
  return z
