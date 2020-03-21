import selenium_krak
res = selenium_krak.get_info('Hartmann')
selenium_krak.save_to_file('\n\n'.join(res))