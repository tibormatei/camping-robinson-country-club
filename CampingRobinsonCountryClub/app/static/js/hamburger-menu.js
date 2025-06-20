// Copyright (c) 2025 Matei Tibor. All rights reserved.
//
//  Filename: hamburger-menu.js
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 2 of the License.

class HamburgerMenu
{
    /**
    * @summary This is the constructor of Hamburger menu class.
    * @param {string} menuButtonId - Hamburger button ID
    * @param {string} mobileMenuContainerId - Menu Bar ID
    */
    constructor(menuButtonId, mobileMenuContainerId)
    {
        this.menuButton = document.querySelector('#' + menuButtonId + ', .' + menuButtonId);
        this.mobileMenuContainer = document.querySelector('#' + mobileMenuContainerId + ', .' + mobileMenuContainerId);

        this.isOpen = false;

        this.menuButton.addEventListener('click', this.toggleMenu.bind(this));
        window.addEventListener('resize', this.removeMobileStyles.bind(this));
    }

    /**
    * @summary This function handles the menu button click event.
    */
    toggleMenu()
    {
        if (this.isOpen == true)
        {
            this.hideSidebar();
            this.isOpen = false;
        }
        else
        {
            this.showSidebar()
            this.isOpen = true;
        }
    }

    /**
    * @summary This function set styles, thats show sidebar.
    */
    showSidebar()
    {
        this.mobileMenuContainer.classList.add('mobile-nav-bar-active');
        this.mobileMenuContainer.style.display = 'flex';
    }

    /**
    * @summary This function set styles, thats hide sidebar.
    */
    hideSidebar()
    {
        this.mobileMenuContainer.classList.remove('mobile-nav-bar-active');
        this.mobileMenuContainer.style.display = 'none';
    }

    /**
    * @summary This function removes mobile styles, let CSS handle it if the screen is desctop.
    */
    removeMobileStyles()
    {
        if (window.innerWidth >= 1025)
        {
            this.mobileMenuContainer.classList.remove('mobile-nav-bar-active');
            this.mobileMenuContainer.style.removeProperty('display');

            this.isOpen = false;
        }
    }
}

// Expose to global scope
window.HamburgerMenu = HamburgerMenu;
