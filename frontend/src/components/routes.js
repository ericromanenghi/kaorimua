import About from './pages/About'
import Home from './pages/Home'
import WorkIndex from './pages/Work/WorkIndex'
import WorkShow from './pages/Work/WorkShow'
import Contact from './pages/Contact'

export const routes = [
    { 
        path: '/', 
        component: Home,
    },
    { 
        path: '/about', 
        component: About,
        meta: {
            title: 'About'
        }
    },
    { 
        path: '/work', 
        component: WorkIndex,
        meta: {
            title: 'Work'
        }
    },
    {
        path: '/work/:id',
        component: WorkShow,
        meta: {
            title: 'Work'
        }
    },
    { 
        path: '/contact', 
        component: Contact,
        meta: {
            title: 'Contact'
        }
    }
]
