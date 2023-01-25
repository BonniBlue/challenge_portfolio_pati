# Task 1: software configuration.
## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

I have a little experience in web development, 
and I`ve been wanting for a long time to get to know more closely with such an IT branch as QA, 
coz I like what QA is doing, like specific of such job and I heard about the great prospects of this profession. 
When I accidentally saw your challenge add on Instagram, 
I realized that this is a great opportunity to get acquainted with this profession, 
master the basics of testing, take out unique insight, get support from skilled mentors, 
communicate with other like-minded people,  
challenge myself, of course, and get the opportunity to grow in IT. 
I'm ready to do my best during the challenge, coz no pain - no gain 	:blush:

# TASK 2: selectors. 

## title_scouts_panel_xpath
//h5[contains(@class,'MuiTypography-h5')] <br />
//h5[text()='Scouts Panel'] <br />
//div[@id='__next'] //descendant::h5

## login_field_xpath
//*[@id='login'] <br />
//input[@name='login'] <br />
//*[@type='text' and @id='login'] <br />
//div[@id='__next'] //descendant::input[@id='login']

## password_field_xpath
//*[@id='password'] <br />
//input[@name='password'] <br />
//*[@type='password']

## button_remind_xpath
//*[@id='__next']/form/div/div[1]/a <br />
//*[text()="Remind password"] <br />
//*[@id='__next']//*[text()='Remind password'] <br />
//*[@id='__next']/descendant::a[contains(@class,'MuiLink-root')]

## button_language_selector_xpath
//*[@aria-haspopup='listbox'] <br />
//*[@id='__next']/form/div/div[2]/div/div <br />
//*[contains(@class,'MuiInputBase-root')]/*[@aria-haspopup='listbox'] <br />
//*[@type='submit']//preceding::div[contains(@class,'MuiSelect-select')] <br />
//*[@id="__next"]/descendant::*[contains(@class,'MuiSelect-select')]

## button_sign_in_xpath
//*[@type='submit'] <br />
//*[contains(@class,'MuiButton-root')] <br />
//*[@type='submit' and contains(@class,'MuiButton-root')] <br />
//*[@id="__next"]/descendant::*[contains(@class,'MuiButton-root')]