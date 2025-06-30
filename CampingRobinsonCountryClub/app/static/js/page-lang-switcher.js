// Copyright (c) 2025 Matei Tibor. All rights reserved.
//
//  Filename: page-lang-switcher.js
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 2 of the License.

class PageLangSwitcher
{
    /**
    * @summary This is the constructor of Page Language Switcher class.
    * @param {string} languageSelectId - Select ID
    */
    constructor(languageSelectId)
    {
        this.languageSelect = document.querySelector('#' + languageSelectId + ', .' + languageSelectId);

        this.languageSelect.addEventListener('change', this.languageSelected.bind(this));
        window.addEventListener('load', this.pageReloadSetCorrectValueForSelect.bind(this));
    }

    /**
    * @summary This function handles the selected value changed event.
    */
    async languageSelected()
    {
        this.setLanguageCookie();

        const url = '/data/languages/' + this.languageSelect.value + '.json';
        fetch(url)
            .then(response => response.json())
            .then(data => this.changePagelanguage(data))
            .catch(error => console.error('Error in languageSelected:', error));
    }

    /**
    * @summary This function set the language cookie.
    */
    setLanguageCookie()
    {
        let data = new Date();
        data.setFullYear(data.getFullYear() + 6);
        document.cookie = "language=" + this.languageSelect.value + "; expires=" + data.toUTCString() + "; path=/";

        console.log("language cookie was set by user");
    }

    /**
    * @summary This function change all text on the page.
    * @param {Object} languageJson - A Json file with selected language.
    */
    changePagelanguage(languageJson)
    {
        const htmlTag = document.querySelector('html');
        htmlTag.lang = languageJson['langCode'];

        // menu
        const regexpMenu = new RegExp('M+.*');
        const headerMobileMenuButton = document.getElementsByClassName('header-mobile-menu-button')[0];
        headerMobileMenuButton.innerText = headerMobileMenuButton.innerText.replace(regexpMenu, languageJson['menu']);

        // rentalDetails section:
        // tentDetails:
        const tentTablePersonHeadere = document.getElementById('rentaldetails-tent-table-thead-personheader');
        tentTablePersonHeadere.innerText = languageJson['rentalDetails']['tentDetails']['personHeader'];

        const tentTableLeiHeadere = document.getElementById('rentaldetails-tent-table-thead-lei');
        tentTableLeiHeadere.innerText = (languageJson['rentalDetails']['tentDetails']['lei'] + languageJson['rentalDetails']['tentDetails']['priceDetail'])

        const tentTableEurHeadere = document.getElementById('rentaldetails-tent-table-thead-eur');
        tentTableEurHeadere.innerText = (languageJson['rentalDetails']['tentDetails']['eur'] + languageJson['rentalDetails']['tentDetails']['priceDetail'])

        const regexpPerson = new RegExp('[A-Z]{1}[a-zá-űă-ț]*');
        const tentTableTds = document.getElementById('rentaldetails-tent-table').getElementsByTagName('td');
        for (const td of tentTableTds)
        {
            td.innerText = td.innerText.replace(regexpPerson, languageJson['rentalDetails']['tentDetails']['personName']);
        }

        // trailerDetails:
        const trailerTablePersonHeadere = document.getElementById('rentaldetails-trailer-table-thead-personheader');
        trailerTablePersonHeadere.innerText = languageJson['rentalDetails']['trailerDetails']['personHeader'];

        const trailerTableLeiHeadere = document.getElementById('rentaldetails-trailer-table-thead-lei');
        trailerTableLeiHeadere.innerText = languageJson['rentalDetails']['trailerDetails']['lei'];

        const trailerTableEurHeadere = document.getElementById('rentaldetails-trailer-table-thead-eur');
        trailerTableEurHeadere.innerText = languageJson['rentalDetails']['trailerDetails']['eur'];

        const trailerTableTds = document.getElementById('rentaldetails-trailer-table').getElementsByTagName('td');
        for (const td of trailerTableTds)
        {
            td.innerText = td.innerText.replace(regexpPerson, languageJson['rentalDetails']['trailerDetails']['personName']);
        }

        // dogDetails:
        const dogTableLeiHeadere = document.getElementById('rentaldetails-dog-table-thead-lei');
        dogTableLeiHeadere.innerText = languageJson['rentalDetails']['dogDetails']['lei'];

        const dogTableEurHeadere = document.getElementById('rentaldetails-dog-table-thead-eur');
        dogTableEurHeadere.innerText = languageJson['rentalDetails']['dogDetails']['eur'];

        const regexpDog = new RegExp('^[A-Z]{1}.*');
        const regexpPriceDetail = new RegExp(' / .*');
        const dogTableTds = document.getElementById('rentaldetails-dog-table').getElementsByTagName('td');
        for (const td of dogTableTds)
        {
            if (regexpDog.test(td.innerText))
            {
                td.innerText = td.innerText.replace(regexpDog, languageJson['rentalDetails']['dogDetails']['dog']);
            }
            else
            {
                if (regexpPriceDetail.test(td.innerText))
                {
                    td.innerText = td.innerText.replace(regexpPriceDetail, languageJson['rentalDetails']['dogDetails']['priceDetail']);
                }
            }
        }

        // priceInformation:
        const priceinformationP = document.getElementById('rentaldetails-priceinformation').querySelector('p');
        if (priceinformationP != null)
        {
            priceinformationP.innerText = languageJson['rentalDetails']['priceInformation'];
        }

        // checkOutinformation:
        const checkoutinformationP = document.getElementById('rentaldetails-checkoutinformation').querySelector('p');
        if (checkoutinformationP != null)
        {
            checkoutinformationP.innerText = languageJson['rentalDetails']['checkOutinformation'];
        }
    }

    /**
    * @summary This function handles the selector when page reload.
    */
    pageReloadSetCorrectValueForSelect()
    {
        const htmlTag = document.querySelector('html');
        this.languageSelect.value = htmlTag.lang;
    }
}

// Expose to global scope
window.PageLangSwitcher = PageLangSwitcher;
