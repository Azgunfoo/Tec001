def is_valid_course_code(code: str) -> bool:
    if len(code) != 6:
        return False
    
    for i in range(3):
        if not code[i].isupper() or not code[i].isalpha():
            return False
            
    for i in range(3, 6):
        if not code[i].isdigit():
            return False
            
    return True