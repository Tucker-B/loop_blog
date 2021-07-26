let posts_li_elements_two = document.querySelectorAll(".posts__post");

posts_li_elements_two.forEach((li_element) => {
    li_id = li_element.id;
    let svg_button = document.querySelector(`#${li_id} .posts__buttons a:last-of-type`);
    svg_button.addEventListener('click', () => {
        let modal_element = document.querySelector('#modal');
        modal_element.style.display = 'block';

        let modal_box_yes_element = document.querySelector('#modal-box__yes');

        let modal_box_yes_element_a = modal_box_yes_element.parentElement;

        let li_slug_id = li_element.id;
        
        // CHANGE HARDCODED ADDRESS FOR DEPLOYMENT
        modal_box_yes_element_a['href'] = `http://127.0.0.1:8000/posts/${li_slug_id}/delete`;

        modal_element.addEventListener('click', () => {
            modal_element.style.display = 'none';
        })
    });
});