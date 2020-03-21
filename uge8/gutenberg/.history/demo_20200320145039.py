import selenium_gutenberg
res = selenium_gutenberg.get_info('sherlock holmes conan')
print("----------------------------------------------------")
selenium_gutenberg.save_to_file('\n\n'.join(res))
