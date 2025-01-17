# Указываем название установщика
Name "MatrixCalculator"

# Указываем название выходного файла установщика
OutFile "setup.exe"

# Указываем директорию по умолчанию для установки
InstallDir "$PROGRAMFILES\MatrixCalculator"

# Запрашиваем права администратора для установки
RequestExecutionLevel admin

# Подключаем Modern UI (MUI2)
!include "MUI2.nsh"

# Указываем текст лицензии
LicenseText "Пожалуйста, прочитайте лицензионное соглашение перед установкой."
LicenseData "license.txt"  # Укажите путь к файлу с лицензией

# Добавляем страницу с лицензией
!insertmacro MUI_PAGE_LICENSE "license.txt"

# Добавляем страницу с директорией установки
!insertmacro MUI_PAGE_DIRECTORY

# Добавляем страницу с компонентами (для выбора ярлыка и папки в меню "Пуск")
!insertmacro MUI_PAGE_COMPONENTS

# Добавляем страницу с установкой
!insertmacro MUI_PAGE_INSTFILES

# Устанавливаем русский язык
!insertmacro MUI_LANGUAGE "Russian"

# Секция для установки программы
Section
  # Создаем директорию для установки
  SetOutPath "$INSTDIR"

  # Копируем файлы программы в директорию установки
  File "C:\Users\Dmitry\PycharmProjects\MatrixCalculator\dist\Matrix_calc.exe"

  # Копируем иконку в корневую директорию
  File "C:\Users\Dmitry\PycharmProjects\MatrixCalculator\dist\icon.ico"

  # Создаем файл для удаления программы
  WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

# Секция для создания ярлыка на рабочем столе
Section "Создать ярлык на рабочем столе" SecDesktopShortcut
  CreateShortcut "$DESKTOP\MatrixCalculator.lnk" "$INSTDIR\Matrix_calc.exe" "" "$INSTDIR\icon.ico" 0 "" "" "$INSTDIR"
SectionEnd

# Секция для создания папки в меню 'Пуск'
Section "Создать папку в меню 'Пуск'" SecStartMenu
  CreateDirectory "$SMPROGRAMS\MatrixCalculator"
  CreateShortcut "$SMPROGRAMS\MatrixCalculator\MatrixCalculator.lnk" "$INSTDIR\Matrix_calc.exe" "" "$INSTDIR\icon.ico" 0 "" "" "$INSTDIR"
  CreateShortcut "$SMPROGRAMS\MatrixCalculator\Uninstall MatrixCalculator.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\icon.ico" 0 "" "" "$INSTDIR"
SectionEnd

# Секция для удаления программы
Section "Uninstall"
  # Отображаем диалоговое окно с подтверждением удаления
  MessageBox MB_YESNO "Вы уверены, что хотите удалить MatrixCalculator?" IDNO noUninstall

  # Удаляем файлы программы
  Delete "$INSTDIR\Matrix_calc.exe"

  # Удаляем папки с иконками
  RMDir /r "$INSTDIR\icon"

  # Удаляем ярлык с рабочего стола (если он был создан)
  Delete "$DESKTOP\MatrixCalculator.lnk"

  # Удаляем запись из меню "Пуск" (если она была создана)
  Delete "$SMPROGRAMS\MatrixCalculator\MatrixCalculator.lnk"
  Delete "$SMPROGRAMS\MatrixCalculator\Uninstall MatrixCalculator.lnk"
  RMDir "$SMPROGRAMS\MatrixCalculator"

  # Удаляем файл для удаления программы
  Delete "$INSTDIR\uninstall.exe"

  # Удаляем директорию установки
  RMDir /r "$INSTDIR"

  # Переход к метке noUninstall, если пользователь выбрал "Нет"
  noUninstall:
SectionEnd