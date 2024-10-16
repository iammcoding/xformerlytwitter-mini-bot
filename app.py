from seleniumbase import SB

username = "tester46384"
password = "50465550Fb++"

with SB(uc=True) as sb:
    sb.open("https://x.com/i/flow/login")

    while True:
        try:
            username_input = sb.wait_for_element('input[autocomplete="username"]', timeout=10)
            if username_input:
                username_input.send_keys(username)

            sb.sleep(2)

            next_username_button = sb.wait_for_element('button:contains("Next")', timeout=10)
            if next_username_button:
                next_username_button.click()


            sb.sleep(2)

            password_input  = sb.wait_for_element('input[name="password"]', timeout=10)
            if password_input:
                password_input.send_keys(password)
            
            sb.sleep(2)

            login_button = sb.wait_for_element('button:contains("Log in")',timeout=10)
            if login_button:
                login_button.click()
            
            sb.sleep(2)

            sb.wait_for_element('.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu', timeout=10)

            while True:
                total_posts = sb.execute_script('return document.querySelectorAll(".css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu").length')

                if total_posts == 0:
                    print("No more posts to like")
                    break

                for index in range(total_posts):
                    sb.sleep(5)
                    sb.execute_script(f'document.querySelectorAll(".css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")[{index}].scrollIntoView();')
                    sb.sleep(5)
                    sb.execute_script(f'document.querySelectorAll(".css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu")[{index}].click()')
                    sb.wait_for_element('button[data-testid="like"]', timeout=10)
                    sb.click('button[data-testid="like"]')
                    sb.sleep(5)
                    sb.go_back()

                sb.refresh()
                sb.sleep(5)
                sb.wait_for_element('.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu', timeout=10)

        except Exception as e:
            print("Something went wrong:", e)
            break