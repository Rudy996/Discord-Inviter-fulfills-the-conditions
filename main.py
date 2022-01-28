from selenium import webdriver
import time



options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--incognito")
# options.add_argument("--disable-blink-features")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-plugins-discovery");
# options.add_argument('--profile-directory=Default')
# options.add_argument("--mute-audio")
# options.add_extension("MetaMask.crx")
# options.add_extension("Phantom.crx")
# options.add_argument("--window-size=1920,1080")

# driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)




def work(acc, tokens, i, link, emoji1, channel11, rules111, emotion11, message1, channel21, rules11, mess1, wait, click):
    try:
        while acc > 0:
            try:
                emoji = emoji1
                channel1 = channel11
                emotion1 = emotion11
                rules = rules111
                message = message1
                channel2 = channel21
                rules1 = rules11
                mess = mess1
                click1 = click
                driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
                java1 = 'function login(token) {    setInterval(() => {        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`    }, 50);    setTimeout(() => {        location.reload();    }, 2500);}   '
                java2 = f'login("{tokens[i]}")'
                driver.get("https://discord.com/login")
                time.sleep(3)
                javascript = java1 + java2
                driver.execute_script(javascript)
                time.sleep(2)
                driver.refresh()
                time.sleep(5)
                try:
                    driver.find_element_by_xpath("//input[@name='password']").is_enabled()
                    print("По токену не вошли")
                    print(f"Кривой токен: {tokens[i]}")
                    with open('invalidTokens.txt', 'a') as file:
                        file.writelines(f'{tokens[i]} \n')
                    time.sleep(5)
                    i = i + 1
                    work()

                except:
                    print("Вошли в аккаунт")
                    time.sleep(2)
                add = driver.find_elements_by_class_name("circleIconButton-1VxDrg")
                add[0].click()
                time.sleep(2)
                driver.find_element_by_xpath("//div[@id='app-mount']/div[4]/div[2]/div/div/div/div/div/div/div[3]/button").click()
                time.sleep(2)
                driver.find_element_by_xpath("//input[@name='']").send_keys(link)
                time.sleep(1)
                driver.find_element_by_xpath("//div[@id='app-mount']/div[4]/div[2]/div/div/div/div/div/div/div/div[3]/button").click()
                time.sleep(3)
                try:
                    time.sleep(1)
                    print("Начало проверки 1/2")
                    error1 = driver.find_element_by_class_name("closeIcon-11LhXr").is_enabled()
                    print("Вылезло подтверждение")
                    while error1 == True:
                        driver.find_element_by_class_name("sizeMedium-2bFIHr").click()
                        print("Кликнул на подтверждение")
                        error1 = driver.find_element_by_class_name("closeIcon-11LhXr").is_enabled()
                        time.sleep(3)
                except:
                    print("Проверка на ошибки законечна 1/2")
                try:
                    time.sleep(1)
                    print("Начало проверки 2/2")
                    error = driver.find_element_by_class_name("button-2zaHZ9").is_enabled()
                    print("Вылезло подтверждение")
                    while error == True:
                        driver.find_element_by_class_name("sizeMedium-2bFIHr").click()
                        print("Кликнул на подтверждение")
                        error = driver.find_element_by_class_name("button-2zaHZ9").is_enabled()
                        time.sleep(3)
                except:
                    print("Проверка на ошибки законечна 2/2")
                try:
                    time.sleep(1)
                    print("Начало проверки 1/2")
                    error1 = driver.find_element_by_class_name("closeIcon-11LhXr").is_enabled()
                    print("Вылезло подтверждение")
                    while error1 == True:
                        driver.find_element_by_class_name("sizeMedium-2bFIHr").click()
                        print("Кликнул на подтверждение")
                        error1 = driver.find_element_by_class_name("closeIcon-11LhXr").is_enabled()
                        time.sleep(3)
                except:
                    print("Проверка на ошибки законечна 1/2")
                try:
                    time.sleep(1)
                    print("Начало проверки 2/2")
                    error = driver.find_element_by_class_name("button-2zaHZ9").is_enabled()
                    print("Вылезло подтверждение")
                    while error == True:
                        driver.find_element_by_class_name("sizeMedium-2bFIHr").click()
                        print("Кликнул на подтверждение")
                        error = driver.find_element_by_class_name("button-2zaHZ9").is_enabled()
                        time.sleep(3)
                except:
                    print("Проверка на ошибки законечна 2/2")

                time.sleep(wait)

                while emoji == 1:
                    try:
                        channel = driver.find_elements_by_class_name("mainContent-20q_Hp")
                        channel[channel1].click()
                        time.sleep(5)
                        emotion = driver.find_elements_by_class_name("reactionInner-9eVHJa")
                        emotion[emotion1].click()
                        time.sleep(5)
                        emoji = 0
                        print("Емоджи найдено")

                    except:
                        emoji = 0
                        print("Емоджи не нашел")


                while rules == 1:
                    try:
                        print("Начинаю подтверждать")
                        time.sleep(2)
                        print("Галочку нажал")
                        driver.find_element_by_class_name("inputDefault-2F39XG").click()
                        time.sleep(2)
                        print("Отправил")
                        driver.find_element_by_class_name("submitButton-34IPxt").click()
                        rules = 0
                        time.sleep(5)
                        print("Принял условия перед отправкой сообщений")
                        while click1 > 0:
                            time.sleep(1)
                            emotion[emotion1].click()
                            time.sleep(0.5)
                            click1 = click1 - 1
                    except:
                        rules = 0
                        print("Подтверждать не нужно перед смайликом")

                while message == 1:
                    channel = driver.find_elements_by_class_name("mainContent-20q_Hp")
                    channel[channel2].click()
                    time.sleep(5)
                    while rules1 == 1:
                        try:
                            time.sleep(2)
                            driver.find_element_by_class_name("button-cO0-d9").click()
                            time.sleep(2)
                            driver.find_element_by_class_name("inputDefault-2F39XG").click()
                            time.sleep(2)
                            driver.find_element_by_class_name("submitButton-34IPxt").click()
                            rules1 = 0
                            time.sleep(5)
                            print("Принял условия перед отправкой сообщений")
                        except:
                            rules1 = 0
                            print("Подтверждать не нужно")
                    try:
                        driver.find_element_by_xpath("//div[@data-slate-object='block']").send_keys(mess,"\n")
                        message = 0
                        print("Сообщение отправлено")
                    except:
                        print("Уже тут был")
                        with open('usedTokens.txt', 'a') as file:
                            file.writelines(f'{tokens[i]} \n')
                        i = i + 1
                        driver.close()
                        work(acc, tokens, i, link, emoji1, channel11, rules111, emotion11, message1, channel21, rules11, mess1, wait, click)
                print(f"Успешний инвайт токена {tokens[i]}")
                with open('validTokens.txt', 'a') as file:
                    file.writelines(f'{tokens[i]} \n')
                time.sleep(5)
                acc = acc - 1
                i = i + 1
                time.sleep(1)

            except Exception as ex:
                print(ex)

            finally:
                driver.close()
                driver.quit()
        else:
            print("Закончил работать")
            driver.quit()
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def rabota():
    # acc = 5
    # token = "OTAyMDMwOTU2NzE2NzczMzc2.YeFlNg.UURHOuHg0D0yDmcZyhSj4Y5YgOQ OTAyMDMwNzA0ODczOTk2MzA4.YeFjOA.cwnwBomx3tpJJznrqmCY61pH5Hs OTAyMDMwNjg2ODU5NDYwNjA4.YeFiSg.Sh-nO289j-tb9lUGgBv_BHBGh6I OTAyMDMwNzAwMjgxMjA0Nzg2.YeE-bA.Z2xnKTOZSBIKWkCuWQiZk3wHSqI OTAyMDMwNTk5ODQ4NjA3Nzc2.YeE5dw.2vTs8f2ZIHA5YHvEMQLVIi-fbCI OTMwMDE3NDE0MDYwNjAxMzQ0.Ydvwmg.C7xtAcTiS_Ncs_47PE0P7JgXXW0"
    # tokens = token.split()
    # link = "https://discord.gg/HPy6FeWp"  # ccылка на дискорд
    # wait = 0
    # i = 0
    # emoji1 = 1  # ставить емоджи?
    # channel11 = 4  # номер канала для емоджи
    # emotion11 = 0  # какой по счету
    # rules111 = 1  # надо подтвердить правила ?
    # click = 1
    # message1 = 0  # нужно оставить сообщение?
    # channel21 = 0  # куда отправтиь сообщение
    # rules11 = 0  # проверка правил при сообщение
    # mess1 = ""


    acc = int(input("Invites: "))
    token = input("Tokens: ")
    tokens = token.split()
    link = input("Ссылка: ")  # ccылка на дискорд
    wait = int(input("Нужно время ожидание после вступление в канал?(если нет пишем 0, время указываем в секундах): "))
    i = 0
    emoji15 = int(input("Емоджи ставим? 1 - да | 0 - нет: "))  # ставить емоджи?
    while emoji15 == 1:
        channel11 = int(input("Номер канала: "))  # номер канала для емоджи
        emotion11 = int(input("Номер емоджи: "))  # какой по счету
        click = int(input("Кол-во кликов по емоджи после подтверждения правил: "))
        rules111 = int(input("Нужно подтвердить правила? 1 - да | 0 - нет: "))  # надо подтвердить правила ?
        emoji1 = 1
        emoji15 = 0
        message15 = int(input("Нужно оставить сообщение? 1 - да | 0 - нет: "))  # нужно оставить сообщение?
        while message15 == 1:
            channel21 = int(input("Номер канала для отправки сообщения: "))  # куда отправтиь сообщение
            rules11 = int(
                input(
                    "Есть проверка правил перед отправкой сообщения? 1 - да | 0 - нет: "))  # проверка правил при сообщение
            mess1 = input("Сообщение: ")
            message1 = 1
            message15 = 0
            work(acc, tokens, i, link, emoji1, channel11, rules111, emotion11, message1, channel21, rules11, mess1,
                 wait, click)
        else:
            message1 = 0  # нужно оставить сообщение?
            channel21 = 0  # куда отправтиь сообщение
            rules11 = 0  # проверка правил при сообщение
            mess1 = ""
            work(acc, tokens, i, link, emoji1, channel11, rules111, emotion11, message1, channel21, rules11, mess1,
                 wait, click)
    else:
        emoji1 = 0
        channel11 = 0  # номер канала для емоджи
        emotion11 = 0  # какой по счету
        rules111 = 0  # надо подтвердить правила ?
        click = 0
    message15 = int(input("Нужно оставить сообщение? 1 - да | 0 - нет: "))  # нужно оставить сообщение?
    while message15 == 1:
        channel21 = int(input("Номер канала для отправки сообщения: "))  # куда отправтиь сообщение
        rules11 = int(
            input("Есть проверка правил перед отправкой сообщения? 1 - да | 0 - нет: "))  # проверка правил при сообщение
        mess1 = input("Сообщение: ")
        message1 = 1
        message15 = 0
        work(acc, tokens, i, link, emoji1, channel11, rules111, emotion11, message1, channel21, rules11, mess1, wait,
             click)
    else:
        emoji1 = 0
        channel21 = 0
        rules11 = 0
        mess1 = 0
        message1 = 0
        message15 = 0
    work(acc, tokens, i, link, emoji1, channel11,rules111, emotion11, message1, channel21, rules11, mess1, wait, click)


rabota()


### Проверка на новый акк ###
# try:
#     driver.find_element_by_xpath("//input[@name='password']").is_enabled()
#     print("По токену не вошли")
#     print(f"Кривой токен: {tokens[i]}")
#     with open('invalidTokens.txt', 'a') as file:
#         file.writelines(f'{tokens[i]} \n')
#     time.sleep(5)
#     acc = acc - 1
#     i = i + 1
#     work()
# except:
#     print("Вошли в аккаунт")
# try:
#     print("Проверка на новый аккаунт")
#     error2 = driver.find_element_by_class_name("closeButton-2LT0iE").is_enabled()
#     time.sleep(1)
#     while error2 == True:
#         error2.click()
#         time.sleep(0.5)
#         error2 = driver.find_element_by_class_name("closeButton-2LT0iE").is_enabled()
# except:
#     print("Проверка закончена")
# try:
#     print("Ищу знак восклицания")
#     time.sleep(3)
#     error3 = driver.find_element_by_xpath(
#         "//div[@id='app-mount']/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[4]/div[2]/div/div[3]").click()
#     error3 = driver.find_element_by_xpath(
#         "//div[@id='app-mount']/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[4]/div[2]/div/div[3]").click()
#     print(error3.text)
#     time.sleep(1)
#     while error3 == True:
#         print("da ???")
#         time.sleep(1)
#         error3.click()
#         error3 = driver.find_element_by_xpath("//div[@aria-controls='popout_38']").is_enabled()
# except:
#     print("Закончена проверка 2")