# 아키텍처별로 사용할 모듈을 가져옵니다.
import platform
import os
import shutil

# 현재 아키텍처를 확인합니다.
architecture = platform.machine()

if architecture == 'x86_64':
    source_directory = '/x86_64/'
elif architecture == 'armv7l':
    source_directory = '/armv7l/'
elif architecture == 'aarch64':
    source_directory = '/aarch64/'
else:
    raise ImportError(f"Unsupported architecture: {architecture}")



# 복사할 .so 파일을 저장할 디렉토리 경로
destination_directory = os.getcwd()

# 원본 디렉토리의 모든 파일과 폴더 목록 얻기
file_list = os.listdir(source_directory)

# .so 파일만 필터링
so_files = [file for file in file_list if file.endswith('.so')]

# .so 파일을 목적지 디렉토리로 복사
for so_file in so_files:
    source_file_path = os.path.join(source_directory, so_file)
    destination_file_path = os.path.join(destination_directory, so_file)

    try:
        shutil.copy2(source_file_path, destination_file_path)  # 파일 복사
        print(f"{so_file} 파일을 복사했습니다.")
    except Exception as e:
        print(f"{so_file} 파일 복사 중 오류 발생: {str(e)}")
