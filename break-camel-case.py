# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    new_solution = ''
    for letters in s:
        if letters.islower():
            new_solution += letters
        else:
            new_solution += f' {letters}'
    return new_solution


print(solution('helloWorldMyNameIsHaroon'))
