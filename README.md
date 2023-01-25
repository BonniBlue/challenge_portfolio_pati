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

# TASK 2: selectors 

## <h5 class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom">Scouts Panel</h5>:
//h5[contains(@class,'MuiTypography-h5')]
//h5[text()='Scouts Panel']
//div[@id='__next'] //descendant::h5

## <input aria-invalid="false" id="login" name="login" type="text" class="MuiInputBase-input MuiInput-input" value="">
//*[@id='login']
//input[@name='login']
//*[@type='text' and @id='login']
//div[@id='__next'] //descendant::input[@id='login']

## <input aria-invalid="false" id="password" name="password" type="password" class="MuiInputBase-input MuiInput-input" value="">
//*[@id='password']
//input[@name='password']
//*[@type='password']

## <a class="MuiTypography-root MuiLink-root MuiLink-underlineHover jss29 MuiTypography-colorPrimary" tabindex="-1">Remind password</a>
//*[@id='__next']/form/div/div[1]/a
//*[text()="Remind password"]
//*[@id='__next']//*[text()='Remind password']
//*[@id='__next']/descendant::a[contains(@class,'MuiLink-root')]

## <div class="MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input" tabindex="0" role="button" aria-haspopup="listbox">English</div>
//*[@aria-haspopup='listbox']
//*[@id='__next']/form/div/div[2]/div/div
//*[contains(@class,'MuiInputBase-root')]/*[@aria-haspopup='listbox']
//*[@type='submit']//preceding::div[contains(@class,'MuiSelect-select')]
//*[@id="__next"]/descendant::*[contains(@class,'MuiSelect-select')]

## <button class="MuiButtonBase-root MuiButton-root MuiButton-contained jss30 MuiButton-containedPrimary" tabindex="0" type="submit"><span class="MuiButton-label">Sign in</span><span class="MuiTouchRipple-root"></span></button>
//*[@type='submit']
//*[contains(@class,'MuiButton-root')]
//*[@type='submit' and contains(@class,'MuiButton-root')]
//*[@id="__next"]/descendant::*[contains(@class,'MuiButton-root')]


!!








