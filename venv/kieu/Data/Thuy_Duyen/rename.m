
filename = dir(fullfile('*jpg'));
total_images=numel(filename)
for i=1 : total_images
    f=fullfile(filename(i).name);
    I= imread(f);
    I = imresize(I,[256,256]);  
    %if(size(I,3)==3)
    %   I = rgb2gray(I);
    %end
    if (i == 1)
        Male = [['Thuy_Duyen_0ID'] '.jpg'];
    else
        Male = [[['Thuy_Duyen_'] num2str(i - 1)] '.jpg'];
    end
    imwrite(I, Male);
end
