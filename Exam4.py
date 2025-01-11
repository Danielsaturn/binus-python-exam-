def rerata_nilai_mhs(miley, grade = 0):
    
    grade_sum = sum(grade)
    grade_ov = len(grade)
    
    average = grade_sum / grade_ov
    
    print("Nilai rerata: ", average)
    
    
miley = print("Nilai student 'Miley': 80, 70, 70, 80")
grade = [80, 70, 70, 80]

print(rerata_nilai_mhs(miley, grade))
