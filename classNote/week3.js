list_of_names = ['Tolu', 'Ibukun', 'Marvellous', "Joshua", "Peter", "Ajayi", 'Jeremiah', 'Steven', 'Emmanuel']
count = 0;

for (each_name of list_of_names) {
    count++
    if (each_name.length == 6) continue
    console.log(`${count}. ${each_name}`)
}