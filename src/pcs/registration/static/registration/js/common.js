calcHeight();
addCurrent();
logoScrollEvent();
heroClickEvent();
mobMenuClickEvent();


function logoScrollEvent() {
    window.addEventListener('scroll', () => {
        let fsu = document.querySelector('div.fsu') || document.querySelector('div.fsu-hide');
        if (window.scrollY > 100)
            fsu.className = 'fsu-hide';
        else
            fsu.className = 'fsu';
    });
    
};

function mobMenuClickEvent() {
    let innerMenu = document.querySelector('div#mobile'),
        menu = document.querySelector('div.menu');
    document.querySelector('div.menu-icon').addEventListener('click', () => {
            if (!innerMenu.className.includes('active')) {
                innerMenu.className += '-active';
                menu.className += '-show';
            }
            else {
                innerMenu.className = 'inner';
                menu.className = 'menu';
            }
        }
    );
};

function heroClickEvent() {
    if (window.location.href.includes('/')) {
        document.querySelector('div.to-content').addEventListener('click', () => {
            document.querySelector('div.content').scrollIntoView({
                behavior: 'smooth'
            });
        });
    }
};

function calcHeight() {
    let navHeight = document.querySelector('header').getBoundingClientRect().height,
        footerHeight = document.querySelector('footer').getBoundingClientRect().height,
        container = document.querySelector('div.container'),
        containerStyle = window.getComputedStyle(container);
    
    let containerHeight = ['height', 'padding-top', 'padding-bottom', 'margin-top', 'margin-bottom']
        .map(key => {
            parseInt(containerStyle.getPropertyValue(key), 10)
        })
        .reduce((prev, curr) => {
            prev + curr
        });

    if (window.location.pathname == '/')
    {
        document.querySelector('div.hero').style.height = String(window.innerHeight - navHeight) + 'px';
        document.querySelector('div.content').style.height = String(window.innerHeight - navHeight - footerHeight) + 'px';
    }  
    else
        document.querySelector('div.content').style.height = String(window.innerHeight) + 'px';
};

function addCurrent() {
    let current = document.querySelectorAll('div.menu > ul > li > a') 
        || document.querySelectorAll('nav > .menu-show > ul > li > a');
    for (let i=0; i < current.length; i++) {
        if (current[i].href == window.location.href) {
            current[i].classList.add('current');
        }
    }   
};

