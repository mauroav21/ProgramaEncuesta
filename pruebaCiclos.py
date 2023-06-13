from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


# Ruta del driver#

# Ruta del controlador de Microsoft Edge
edge_driver_path = 'C:/Users/mauro/OneDrive/Documentos/programas/ProgramaEncuesta/msedgedriver.exe'

# Opciones del navegador
options = webdriver.EdgeOptions()
options.use_chromium = True

# Configurar el controlador de Microsoft Edge
driver = webdriver.Edge(executable_path=edge_driver_path, options=options)


# Ruta del forulario#
driver.get('https://itsaltillo.mindbox.app/login/alumno')

# Usuario


campo_texto_user = driver.find_element(By.ID, "ncontrol")
campo_texto_user.send_keys('')
driver.find_element
# Contraeña
campo_texto_pwd = driver.find_element(By.ID, 'password')
campo_texto_pwd.send_keys('')

# Click boton login
boton_login = driver.find_element(By.CLASS_NAME,'btn')
boton_login.click()

time.sleep(10)

# Click evaluaciones
buscador_evaluaciones = driver.find_element(By.ID, 'menu-search-bar')
buscador_evaluaciones.click()

# Insertar texto en buscador
buscador_evaluaciones_text = driver.find_element(By.TAG_NAME, 'input')
buscador_evaluaciones_text.send_keys('Evaluación docente')
time.sleep(3)

# Click opcion
buscador_evaluacion_docenteA = driver.find_element(By.ID, 'search-result-container')
buscador_evaluacion_docenteA.click()

time.sleep(3)


# Click en continuar
click_continuar = driver.find_element(By.CLASS_NAME, 'fa.fa-arrow-right')
click_continuar.click()

time.sleep(7)

# Función para seleccionar una opción y esperar 1 segundo
def seleccionar_opcion(xpath):
    seleccionar_op = Select(driver.find_element(By.XPATH, xpath))
    seleccionar_op.select_by_value('5')
    print('Si, también llegamos hasta aquí')
    time.sleep(1)

# Secciones y sus correspondientes XPaths

#
# 1/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]', '//*[@id="answer_q4_Af3"]', '//*[@id="answer_q5_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]', '//*[@id="answer_q4_Bf3"]', '//*[@id="answer_q5_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]', '//*[@id="answer_q4_Cf5"]', '//*[@id="answer_q5_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]', '//*[@id="answer_q4_Df3"]', '//*[@id="answer_q5_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]', '//*[@id="answer_q4_Df8"]', '//*[@id="answer_q5_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]', '//*[@id="answer_q4_Ff4"]', '//*[@id="answer_q5_Ff4"]']
}

# Iterar sobre las secciones y sus XPaths
for seccion, xpaths in secciones.items():
    print('Si llegamos hasta aquí')
    for xpath in xpaths:
        seleccionar_opcion(xpath)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 2/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]']
}

for seccion, xpaths in secciones.items():
    for xpath in xpaths:
        seleccionar_op = Select(driver.find_element(By.XPATH, xpath))
        seleccionar_op.select_by_value('5')
        print('Si, también llegamos hasta aquí')
        time.sleep(1)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 3/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]', '//*[@id="answer_q4_Af3"]', '//*[@id="answer_q5_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]', '//*[@id="answer_q4_Bf3"]', '//*[@id="answer_q5_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]', '//*[@id="answer_q4_Cf5"]', '//*[@id="answer_q5_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]', '//*[@id="answer_q4_Df3"]', '//*[@id="answer_q5_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]', '//*[@id="answer_q4_Df8"]', '//*[@id="answer_q5_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]', '//*[@id="answer_q4_Ff4"]', '//*[@id="answer_q5_Ff4"]']
}

# Iterar sobre las secciones y sus XPaths
for seccion, xpaths in secciones.items():
    print('Si llegamos hasta aquí')
    for xpath in xpaths:
        seleccionar_opcion(xpath)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 4/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]', '//*[@id="answer_q4_Af3"]', '//*[@id="answer_q5_Af3"]', '//*[@id="answer_q6_Af3"]', '//*[@id="answer_q7_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]', '//*[@id="answer_q4_Bf3"]', '//*[@id="answer_q5_Bf3"]', '//*[@id="answer_q6_Bf3"]', '//*[@id="answer_q7_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]', '//*[@id="answer_q4_Cf5"]', '//*[@id="answer_q5_Cf5"]', '//*[@id="answer_q6_Cf5"]', '//*[@id="answer_q7_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]', '//*[@id="answer_q4_Df3"]', '//*[@id="answer_q5_Df3"]', '//*[@id="answer_q6_Df3"]', '//*[@id="answer_q7_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]', '//*[@id="answer_q4_Df8"]', '//*[@id="answer_q5_Df8"]', '//*[@id="answer_q6_Df8"]', '//*[@id="answer_q7_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]', '//*[@id="answer_q4_Ff4"]', '//*[@id="answer_q5_Ff4"]', '//*[@id="answer_q6_Ff4"]', '//*[@id="answer_q7_Ff4"]']
}

# Iterar sobre las secciones y sus XPaths
for seccion, xpaths in secciones.items():
    print('Si llegamos hasta aquí')
    for xpath in xpaths:
        seleccionar_opcion(xpath)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 5/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]', '//*[@id="answer_q4_Af3"]', '//*[@id="answer_q5_Af3"]', '//*[@id="answer_q6_Af3"]', '//*[@id="answer_q7_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]', '//*[@id="answer_q4_Bf3"]', '//*[@id="answer_q5_Bf3"]', '//*[@id="answer_q6_Bf3"]', '//*[@id="answer_q7_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]', '//*[@id="answer_q4_Cf5"]', '//*[@id="answer_q5_Cf5"]', '//*[@id="answer_q6_Cf5"]', '//*[@id="answer_q7_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]', '//*[@id="answer_q4_Df3"]', '//*[@id="answer_q5_Df3"]', '//*[@id="answer_q6_Df3"]', '//*[@id="answer_q7_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]', '//*[@id="answer_q4_Df8"]', '//*[@id="answer_q5_Df8"]', '//*[@id="answer_q6_Df8"]', '//*[@id="answer_q7_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]', '//*[@id="answer_q4_Ff4"]', '//*[@id="answer_q5_Ff4"]', '//*[@id="answer_q6_Ff4"]', '//*[@id="answer_q7_Ff4"]']
}

# Iterar sobre las secciones y sus XPaths
for seccion, xpaths in secciones.items():
    print('Si llegamos hasta aquí')
    for xpath in xpaths:
        seleccionar_opcion(xpath)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 6/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]', '//*[@id="answer_q4_Af3"]', '//*[@id="answer_q5_Af3"]', '//*[@id="answer_q6_Af3"]', '//*[@id="answer_q7_Af3"]', '//*[@id="answer_q8_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]', '//*[@id="answer_q4_Bf3"]', '//*[@id="answer_q5_Bf3"]', '//*[@id="answer_q6_Bf3"]', '//*[@id="answer_q7_Bf3"]', '//*[@id="answer_q8_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]', '//*[@id="answer_q4_Cf5"]', '//*[@id="answer_q5_Cf5"]', '//*[@id="answer_q6_Cf5"]', '//*[@id="answer_q7_Cf5"]', '//*[@id="answer_q8_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]', '//*[@id="answer_q4_Df3"]', '//*[@id="answer_q5_Df3"]', '//*[@id="answer_q6_Df3"]', '//*[@id="answer_q7_Df3"]', '//*[@id="answer_q8_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]', '//*[@id="answer_q4_Df8"]', '//*[@id="answer_q5_Df8"]', '//*[@id="answer_q6_Df8"]', '//*[@id="answer_q7_Df8"]', '//*[@id="answer_q8_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]', '//*[@id="answer_q4_Ff4"]', '//*[@id="answer_q5_Ff4"]', '//*[@id="answer_q6_Ff4"]', '//*[@id="answer_q7_Ff4"]', '//*[@id="answer_q8_Ff4"]']
}

# Iterar sobre las secciones y sus XPaths
for seccion, xpaths in secciones.items():
    print('Si llegamos hasta aquí')
    for xpath in xpaths:
        seleccionar_opcion(xpath)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 7/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]']
}

for seccion, xpaths in secciones.items():
    for xpath in xpaths:
        seleccionar_op = Select(driver.find_element(By.XPATH, xpath))
        seleccionar_op.select_by_value('5')
        print('Si, también llegamos hasta aquí')
        time.sleep(1)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 8/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]', '//*[@id="answer_q4_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]', '//*[@id="answer_q4_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]', '//*[@id="answer_q4_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]', '//*[@id="answer_q4_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]', '//*[@id="answer_q4_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]', '//*[@id="answer_q4_Ff4"]']
}

# Iterar sobre las secciones y sus XPaths
for seccion, xpaths in secciones.items():
    print('Si llegamos hasta aquí')
    for xpath in xpaths:
        seleccionar_opcion(xpath)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 9/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]']
}

for seccion, xpaths in secciones.items():
    for xpath in xpaths:
        seleccionar_op = Select(driver.find_element(By.XPATH, xpath))
        seleccionar_op.select_by_value('5')
        print('Si, también llegamos hasta aquí')
        time.sleep(1)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 10/11
#
#

secciones = {
    'Calculo': ['//*[@id="answer_q1_Af3"]', '//*[@id="answer_q2_Af3"]', '//*[@id="answer_q3_Af3"]'],
    'ED': ['//*[@id="answer_q1_Bf3"]', '//*[@id="answer_q2_Bf3"]', '//*[@id="answer_q3_Bf3"]'],
    'TBD': ['//*[@id="answer_q1_Cf5"]', '//*[@id="answer_q2_Cf5"]', '//*[@id="answer_q3_Cf5"]'],
    'IO': ['//*[@id="answer_q1_Df3"]', '//*[@id="answer_q2_Df3"]', '//*[@id="answer_q3_Df3"]'],
    'Progra Web': ['//*[@id="answer_q1_Df8"]', '//*[@id="answer_q2_Df8"]', '//*[@id="answer_q3_Df8"]'],
    'Principios Electricos': ['//*[@id="answer_q1_Ff4"]', '//*[@id="answer_q2_Ff4"]', '//*[@id="answer_q3_Ff4"]']
}

for seccion, xpaths in secciones.items():
    for xpath in xpaths:
        seleccionar_op = Select(driver.find_element(By.XPATH, xpath))
        seleccionar_op.select_by_value('5')
        print('Si, también llegamos hasta aquí')
        time.sleep(1)

boton_continuar_e1 = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

#
# 11/11
#
#

campo_texto_op = driver.find_element(By.ID, 'answer_Af3')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Bf3')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Cf5')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Df3')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Df8')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Ff4')
campo_texto_op.send_keys('excelente')

boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)