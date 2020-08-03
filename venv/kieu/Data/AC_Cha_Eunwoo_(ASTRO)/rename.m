
filename = dir(fullfile('*.jpg'));
total_images=numel(filename)
for i=1 : total_images
    f=fullfile(filename(i).name);
    I= imread(f);
    I = imresize(I,[256,256]);  
    %if(size(I,3)==3)
    %   I = rgb2gray(I);
    %end
    if (i == 1)
        Male = [['Cha_Eunwoo_(ASTRO)_0ID'] '.jpg'];
    else
        Male = [[['Cha_Eunwoo_(ASTRO)_'] num2str(i - 1)] '.jpg'];
    end
    imwrite(I, Male);
end
