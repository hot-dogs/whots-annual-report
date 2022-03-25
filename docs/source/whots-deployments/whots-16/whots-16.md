# WHOTS-16

This will become whots-16 report!

+ THIS IS A TEST!


##  Markdown
### Images 
 
1. Display any image with a link     
`![HOT](https://datadocs.bco-dmo.org/d2/images/logos/logo_HOT.jpg)`, generates the following:

![HOT](https://datadocs.bco-dmo.org/d2/images/logos/logo_HOT.jpg)

2. Download the image locally:
    
    ```shell script
    curl https://datadocs.bco-dmo.org/d2/images/logos/logo_HOT.jpg > _build/hmtl/_images/logo_HOT.jpg 
    ```
    
3. Edit and display:

    + add the following in the `markdown_tips.md` file: 
   
        ````markdown
        ```{image} _build/html/_images/logo_HOT.jpg
        :alt: HOT-2
        :class: bg-primary
        :width: 200px
        :align: center
        ```
        ````
        ```{tip}
         You will notice that the image is now centered in the page
        ```
