<template>
    <div>
        <nav class='navigation' :class="{ 'navigation--active': isMenuOpen }">
            <router-link to='/'>
                <img src='./../../assets/logo.png' alt='Kaori. Makeup Artist'>
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
        <header class='header'>
            <router-link to='/' class='header__logo' :class="{ 'header__logo--hidden': isMenuOpen }">
                <img src='./../../assets/logo.png' alt='Kaori. Makeup Artist'>
            </router-link>
            <button class='header__button' type='button' @click='isMenuOpen = !isMenuOpen'>Menu</button>
        </header>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            isMenuOpen: false,
        }
    },
    methods: {
        toggleMenu () {
            alert('toggle')
        }
    },
    watch: {
        $route() {
            this.isMenuOpen = false
        }
    }
}
</script>

<style scoped lang='scss'>
@import './../../scss/variables.scss';

.header {
    align-items: center;
    display: flex;
    justify-content: space-between;
    padding: 20px;
    width: 100%;
}
.header__logo {
    transition: transform .2s linear;
}
.header__logo--hidden {
    transform: translateX(-100px);
}
.header__logo img {
    width: 100px;
}
.header__button {
    background: transparent;
    border: 0;
    font-family: $font-family
}

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
    transition: transform .2s ease;
    transform: translateX(-300px);
    top: 0;
    width: 300px;
    z-index: 9;
}
.navigation--active {
    transform: translateX(0);
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
    font-size: 1.2em;
    font-weight: bold;
    padding: 5px 0;
    position: relative;
    text-decoration: none;
}
.navigation__item:after {
    background: $color-primary;
    border-radius: 4px;
    content: '';
    display: block;
    height: 2px;
    left: calc(100% + 10px);
    position: absolute;
    top: 50%;
    transition: width .2s ease;
    width: 0;
}
.navigation__item--active {
    color: $color-primary;
}
.navigation__item--active:after {
    width: 40px;
}
.navigation__item:hover {
    color: $color-primary;
}
.navigation__contact {
    font-size: .8em;
    line-height: 1.75;
    margin: 0;
}
.navigation__contact a {
    color: $color-primary;
}
.navigation__contact a:hover {
    text-decoration: none;
}

@media screen and (min-width: 700px) {
    .header {
        display: none;
    }
    .navigation {
        transform: translateX(0);
    }
}
</style>