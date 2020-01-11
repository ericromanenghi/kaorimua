<template>
    <nav class='navigation'>
        <router-link to='/'>
            <img src='./../assets/logo.png' alt='Kaori. Makeup Artist'>
        </router-link>
        <ul class='navigation__list'>
            <li><router-link to='/about' class='navigation__item'>About me</router-link></li>
            <li><router-link to='/work' class='navigation__item'>Work</router-link></li>
            <li><router-link to='/contact' class='navigation__item'>Contact</router-link></li>
        </ul>
        <p class='navigation__contact'>
            +31 614 395 295<br>
            <a href='#'>info@kaorimua.nl</a>
        </p>
    </nav>
</template>

<style scoped lang='scss'>
.navigation {
    align-items: flex-start;
    background: #fff;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-around;
    left: 0;
    padding: 30px;
    position: fixed;
    top: 0;
    width: 300px;
    z-index: 9;
}
.navigation img {
    display: block;
    margin: 0 auto;
    width: 140px;
}
.navigation__list {
    list-style: none;
    margin: 30px 0;
    padding: 0;
}
.navigation__item {
    color: #000;
    display: inline-block;
    font-family: 'Merriweather', serif;
    font-size: 1.2em;
    font-weight: bold;
    padding: 5px 0;
    text-decoration: none;
}
.navigation__item--active {
    color: #E65F9A;
}
.navigation__item:hover {
    color: #E65F9A;
}
.navigation__contact {
    font-family: 'Merriweather', serif;
    font-size: .8em;
    line-height: 1.75;
    margin: 0;
}
.navigation__contact a {
    color: #E65F9A;
}
.navigation__contact a:hover {
    text-decoration: none;
}
</style>