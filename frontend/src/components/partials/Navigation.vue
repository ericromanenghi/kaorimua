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
                +31 614 802 365<br>
                <a href='#'>kaorimua@gmail.com</a>
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

<style scoped lang='scss' src='@/scss/navigation.scss'></style>