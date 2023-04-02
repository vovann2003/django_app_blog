function app() {
    const buttons = document.querySelectorAll('.buttons')
    const recipes = document.querySelectorAll('.recipe-item')

    function filter (category, items) {
        items.forEach((item) => {
            const isRecipeFiltered = !item.classList.contains(category)
            const isShowAll = category.toLowerCase() === 'all'
            if (isRecipeFiltered && !isShowAll) {
                item.classList.add('anime')
            } else {
                item.classList.remove('anime')
            }
        })
    }


    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            const currentCategory = button.dataset.filter
            console.log(currentCategory)
            filter(currentCategory, recipes)
        })
    })


}

app()