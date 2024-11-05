from setuptools import setup

APP = ['your_script.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['numpy', 'matplotlib', 'scipy', 'tkinter'],
    'iconfile': 'icon.icns',  # 아이콘 파일이 있는 경우
    'plist': {
        'CFBundleName': "정규분포계산기",
        'CFBundleShortVersionString': "1.0.0",
        'CFBundleVersion': "1.0.0",
        'CFBundleIdentifier': "com.yourname.normaldistcalc",
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```

3. 실행 파일 생성:
```bash
# 개발 모드로 테스트
python setup.py py2app -A

# 배포용 빌드
python setup.py py2app
```

생성된 앱은 `dist` 폴더에서 찾을 수 있습니다.

추가 팁:
1. 앱 아이콘을 추가하려면 .icns 파일이 필요합니다. png나 jpg 파일을 .icns로 변환할 수 있는 온라인 도구들이 있습니다.
2. 앱이 제대로 실행되지 않는다면 터미널에서 직접 실행해보고 오류 메시지를 확인해보세요.
3. Mac의 보안 설정 때문에 실행이 차단될 수 있습니다. 이 경우 시스템 환경설정 → 보안 및 개인 정보 보호에서 앱 실행을 허용해주어야 합니다.

이렇게 수정하면 Mac에서도 정상적으로 작동할 것입니다. 혹시 다른 오류가 발생하면 알려주세요!