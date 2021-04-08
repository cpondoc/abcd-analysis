type size_and_sex.csv
data = readmatrix('size_and_sex.csv')
head_sizes = data(:,1)
sexes = data(:,2)
z_head_sizes = zscore(head_sizes)
[dx_matched, svol_matched] = matchGroup(transpose(sexes), transpose(z_head_sizes))
final_result = [svol_matched, dx_matched]
writematrix(final_result)

function [dx_matched, svol_matched] = matchGroup(dx_new, svol_new)
%% svol_new is the z-score of head size
%% dx_new is the gender label
interval = 0.5; % adjust this bin size to control matching 
dx_matched = [];
svol_matched = [];
for i = -3:interval:3
	% collect boys and girls in a certain interval (bin)
    idx0 = find(dx_new == 0 & svol_new <= (i+interval) & svol_new > i);
    idx1 = find(dx_new == 1 & svol_new <= (i+interval) & svol_new > i);
    % select an equal maximum number of boys and girls in that bin
    if length(idx0) > length(idx1)
        IDX = randperm(length(idx0));
        idx0 = idx0(IDX(1:length(idx1)));
    else
        IDX = randperm(length(idx1));
        idx1 = idx1(IDX(1:length(idx0)));          	 
    end
    % construct matched set
    dx_matched = [dx_matched;dx_new(idx0)';dx_new(idx1)'];
    svol_matched = [svol_matched;svol_new(idx0)';svol_new(idx1)'];
end
end