from setuptools import setup, find_packages
import os
import shutil

architecture_directory = ['x86_64', 'armv7l', 'aarch64']
target_directory = 'SG1AB'
packaging_directory = ['build', 'dist', target_directory + '.egg-info']

try:
    # remove packaging directory
    for packaging_dir in packaging_directory:
        if os.path.exists(packaging_dir):
                print(f"Deleting existing directory '{packaging_dir}'...")
                shutil.rmtree(packaging_dir)
    
    # remove architectory directory
    if os.path.exists(target_directory):
        for arch_dir in architecture_directory:
            arch_path = os.path.join(target_directory, arch_dir)
            if os.path.exists(arch_path):
                print(f"Deleting existing directory '{arch_path}'...")
                shutil.rmtree(arch_path)
        
        # make architecture_directory and copy .so files to the directories
        for arch_dir in architecture_directory:
            arch_path = os.path.join(target_directory, arch_dir)
            os.makedirs(arch_path)
            print(f"Created directory '{arch_path}'")

            so_dir = os.path.join( '../../../Product', arch_dir + '-linux.release/out/lib')
            so_files = [f for f in os.listdir(so_dir) if f.endswith(".so")]
             
            for so_file in so_files:
                src_path = os.path.join(so_dir, so_file)
                shutil.copy(src_path, arch_path)
                print(f"Copied {so_file} to {arch_path}")
    
            
    print("Operation completed successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")


# copy .so files to architecture directories

setup(
    name=target_directory,
    version='1.0.3.0',
    description='nnfw_api binding',
    long_description='you can use nnfw_api by python',
    url='https://github.com/Samsung/ONE/tree/master/runtime',
    author='Your Name',
    author_email='your@email.com',
    license='Samsung',
    packages=[target_directory],
    package_data={target_directory: ['x86_64/nnfw_api_pybind.cpython-38-x86_64-linux-gnu.so', 'x86_64/libnnfw-dev.so', 'x86_64/libonert_core.so', 'x86_64/libbackend_cpu.so','armv7l/nnfw_api_pybind.cpython-38-arm-linux-gnueabihf.so', 'armv7l/libnnfw-dev.so', 'armv7l/libonert_core.so', 'armv7l/libbackend_cpu.so','aarch64/nnfw_api_pybind.cpython-38-aarch64-linux-gnu.so', 'aarch64/libnnfw-dev.so', 'aarch64/libonert_core.so', 'aarch64/libbackend_cpu.so']},
    install_requires=[
        # 필요한 의존성 패키지를 여기에 추가
    ],
)

