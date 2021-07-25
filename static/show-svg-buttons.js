let posts_li_elements = document.querySelectorAll(".posts__post");
let posts_buttons_svgs = document.querySelectorAll(".posts__buttons svg");

posts_li_elements.forEach((li_element) => {
    li_element.addEventListener('mouseover', () => {
        let li_id_name = li_element.id;
        let button_svgs = document.querySelectorAll(`#${li_id_name} svg`);

        button_svgs.forEach((button_svg) => {
            if (!button_svg.style.visibility) {
                button_svg.style.visibility = "visible";
            }
            else if (button_svg.style.visibility == "hidden") {
                button_svg.style.visibility = "visible";
            } else {
                button_svg.style.visibility = "hidden";
            }
        });
    })
    
    li_element.addEventListener('mouseout', () => {
        let li_id_name = li_element.id;
        let button_svgs = document.querySelectorAll(`#${li_id_name} svg`);
        button_svgs.forEach((button_svg) => {
            button_svg.style.visibility = "hidden";
        });
        
    })
})