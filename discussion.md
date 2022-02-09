# options for variables

## 1. Just serialize them:

  ```"continue_with_apple": [(MobileBy.ID, _not_android), (MobileBy.ID, "createAccountView-signInWithApple-signInWithAppleView")]```

  becomes

  ```"continue_with_apple": [["id", "N/A to Android"], ["id", "createAccountView-signInWithApple-signInWithAppleView"]]```

## 2. If the variable functionality should be preserved, use the % operator:

```{ "current_date": "The current date and time is: %s" } ```

  or in the top case:

  ```"continue_with_apple": [[%(MobileBy.ID)s, %(_not_android)s], [%(MobileBy.ID)s, "createAccountView-signInWithApple-signInWithAppleView"]]```

  which will have to be substituted in the code later by the real variable


